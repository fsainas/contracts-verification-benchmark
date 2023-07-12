// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   bool public isCommitted;
   uint start;

   // ghost variables
   uint _sent;
   uint _deposited;

   // v1
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       isCommitted = false;
   }

   // v1
   function commit(bytes32 h) public payable {
       require(msg.sender == owner);
       require(msg.value >= 1 ether);
       require(!isCommitted);
       hash = h;
       isCommitted = true;

       _deposited = address(this).balance;       
   }

   // v1
   function reveal(string memory s) public {
       require(msg.sender == owner);
       require(keccak256(abi.encodePacked(s)) == hash);
       require(isCommitted);
       
       uint _to_send = address(this).balance;       
       (bool success,) = owner.call{value: _to_send}("");
       require(success, "Transfer failed.");

       _sent += _to_send;
   }

   // v1
   function timeout() public {
       require(block.number > start + 1000);
       require(isCommitted);

       uint _to_send = address(this).balance;
       (bool success,) = verifier.call{value: _to_send}("");
       require(success, "Transfer failed.");

       _sent += _to_send;       
   }

   // p1
   function invariant() public view {
       assert(_sent <= _deposited);
   }   
}
