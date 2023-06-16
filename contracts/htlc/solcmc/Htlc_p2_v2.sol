// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   uint start;

   // ghost variables
   bool _commit_called = false;   
   bool _reveal_called = false;
   bool _timeout_called = false;

   // v2
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
   }

   // v2
   function commit(bytes32 h) public payable {
       require (msg.sender==owner);
       require (msg.value >= 1 ether);

       hash = h;
       // isCommitted = true;
 
       _commit_called = true;
   }

   // v2
   function reveal(string memory s) public {
       require (msg.sender==owner);
       require(keccak256(abi.encodePacked(s))==hash);
       // require (isCommitted);
       
       (bool success,) = owner.call{value: address(this).balance }("");
       require (success, "Transfer failed.");

       _reveal_called = true;      
   }

   // v2
   function timeout() public {
       require (block.number > start + 1000);
       // require (isCommitted);
       
       (bool success,) = verifier.call{value: address(this).balance }("");
       require (success, "Transfer failed.");

       _timeout_called = true;       
   }

   // p2: if timeout or reveal are called, then commit must have been called   
   function invariant() public view {
       assert(!((_timeout_called || _reveal_called) && !_commit_called));
   }
   
}

// ====
// SMTEngine: CHC
// Time: 1.61s
// Targets: "all"
// ----
// Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here - line 37
// Warning: CHC: Assertion violation happens here - line 44
