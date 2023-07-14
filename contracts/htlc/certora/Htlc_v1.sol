// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   bool public isCommitted;
   uint start;
  
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       isCommitted = false;
   }

   function getOwner() public view returns (address) {
       return owner;
   }

   function getBalance() public view returns (uint) {
       return address(this).balance;
   }

   function getStart() public view returns (uint) {
       return start;
   }

   function getIsCommitted() public view returns (bool) {
       return isCommitted;
   }

   function commit(bytes32 h) public payable {
       require(msg.sender == owner);
       require(msg.value >= 1 ether);
       require(!isCommitted);

       hash = h;
       isCommitted = true;
   }

   function reveal(string memory s) public {
       require(msg.sender == owner);
       require(keccak256(abi.encodePacked(s)) == hash);
       require(isCommitted);       

       (bool success,) = owner.call{value: address(this).balance }("");
       require(success, "Transfer failed.");
   }

   function timeout() public {
       require(block.number > start + 1000);
       require(isCommitted);       

       (bool success,) = verifier.call{value: address(this).balance }("");
       require(success, "Transfer failed.");
   }
}
