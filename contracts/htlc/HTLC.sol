// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   bool public isCommitted;
   uint start;

   // ghost variables
   uint _balance;
   uint _sent;
   uint _deposited;
   
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       isCommitted = false;
       _balance = address(this).balance;
   }

   function commit(bytes32 h) public payable {
       require (msg.sender==owner);
       require (msg.value >= 1 ether);
       require (!isCommitted);
       _deposited = msg.value + _balance;      
       hash = h;
       isCommitted = true;       
   }

   function reveal(string memory s) public {
       require (msg.sender==owner);
       require(keccak256(abi.encodePacked(s))==hash);
       require (isCommitted);       
       _sent += _balance;
       _balance -= _sent;
       (bool success,) = owner.call{value: _sent}("");
       require (success, "Transfer failed.");
   }

   function timeout() public {
       require (block.number > start + 1000);
       require (isCommitted);       
       _sent += _balance;
       _balance -= _sent;       
       (bool success,) = verifier.call{value: _sent}("");
       require (success, "Transfer failed.");
   }

   function invariant() public view {
       assert(_sent <= _deposited);
   }
   
}
