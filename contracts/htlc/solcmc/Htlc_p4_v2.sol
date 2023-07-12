// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   //bool public isCommitted;
   uint start;

   // ghost variables
   address _commit_sender;
   bool public _isCommitted;
   
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       //isCommitted = false;
   }

   function commit(bytes32 h) public payable {
       require(msg.value >= 1 ether);
       //require(!isCommitted);
       hash = h;
       _isCommitted = true;
       _commit_sender = msg.sender;
   }

   function reveal(string memory s) public {
       require(msg.sender == owner);
       require(keccak256(abi.encodePacked(s)) == hash);
       //require(isCommitted);       
       (bool success,) = owner.call{value: address(this).balance }("");
       require(success, "Transfer failed.");
   }

   function timeout() public {
       require(block.number > start + 1000);
       //require(isCommitted);
       (bool success,) = verifier.call{value: address(this).balance }("");
       require(success, "Transfer failed.");
   }

   // p4: if commit is called, then the sender must be the owner
   function invariant() public view {
       assert(!_isCommitted || _commit_sender==owner);
   }
   
}
