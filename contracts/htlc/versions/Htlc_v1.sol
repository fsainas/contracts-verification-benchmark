// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.18;

/// @custom:version conformant to specification.
contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   bool public isCommitted;
   uint start;

   // ghost variables
   uint _sent;
   uint _deposited;
   bool _commit_called = false;   
   bool _reveal_called = false;
   bool _timeout_called = false;
   uint _timeout_diff;   
   address _commit_sender;
  
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
       isCommitted = false;
   }

   function commit(bytes32 h) public payable {
       require(msg.sender == owner);
       require(msg.value >= 1 ether);
       require(!isCommitted);

       hash = h;
       isCommitted = true;
        
       // ghost state
       _deposited = address(this).balance;       
       _commit_called = true;
       _commit_sender = msg.sender;
   }

   function reveal(string memory s) public {
       require(msg.sender == owner);
       require(keccak256(abi.encodePacked(s)) == hash);
       require(isCommitted);       

       uint _to_send = address(this).balance;       
       (bool success,) = owner.call{value: _to_send}("");
       require(success, "Transfer failed.");

       // ghost state
       _sent += _to_send;
       _reveal_called = true;            
   }

   function timeout() public {
       require(block.number > start + 1000);
       require(isCommitted);       

       uint _to_send = address(this).balance;
       (bool success,) = verifier.call{value: _to_send}("");
       require(success, "Transfer failed.");

       // ghost state
       _sent += _to_send;       
       _timeout_called = true;      
       _timeout_diff = block.number - start;       
   }
}
