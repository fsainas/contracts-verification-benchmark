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
   
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
   }

   function commit(bytes32 h) public payable {
       require (msg.sender==owner);
       require (msg.value >= 1 ether);
       hash = h;
       _commit_called = true;
   }

   function reveal(string memory s) public {
       require (msg.sender==owner);
       require(keccak256(abi.encodePacked(s))==hash);
       _reveal_called = true;       
       (bool success,) = owner.call{value: address(this).balance }("");
       require (success, "Transfer failed.");
   }

   function timeout() public {
       require (block.number > start + 1000);
       _timeout_called = true;
       (bool success,) = verifier.call{value: address(this).balance }("");
       require (success, "Transfer failed.");
   }

   function invariant() public view {
       assert(!((_timeout_called || _reveal_called) && !_commit_called));
   }
   
}
