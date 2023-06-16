// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.2;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   // bool public isCommitted;
   uint start;

   // ghost variables
   bool _timeout_called;
   uint _timeout_diff;   

   // v2
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       // isCommitted = false;
   }

   // v2
   function commit(bytes32 h) public payable {
       require (msg.sender==owner);
       require (msg.value >= 1 ether);
       // require (!isCommitted);

       hash = h;
       // isCommitted = true;
   }

   // v2
   function reveal(string memory s) public {
       require (msg.sender==owner);
       require (keccak256(abi.encodePacked(s))==hash);
       // require (isCommitted);       

       (bool success,) = owner.call{value: address(this).balance }("");
       require (success, "Transfer failed.");
   }

   // v2
   function timeout() public {
       require (block.number > start + 1000);
       // require (isCommitted);

       (bool success,) = verifier.call{value: address(this).balance }("");
       require (success, "Transfer failed.");

       _timeout_called = true;
       _timeout_diff = block.number - start;       
   }

   // p3: if timeout is called, then at least 1000 blocks have passed since
   // the contract was deployed
   function invariant() public view {
       assert(!_timeout_called || _timeout_diff > 1000);
   }
   
}
