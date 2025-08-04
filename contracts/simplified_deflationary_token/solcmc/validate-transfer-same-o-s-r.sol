function validateTransferSameOSR(address receiver, uint256 amount) public {
   require(owner == msg.sender && msg.sender == receiver);
   uint256 oldSenderBalance = balances[msg.sender];
   uint256 oldReceiverBalance = balances[receiver];
   uint256 oldOwnerBalance = balances[owner];
  
   require(oldOwnerBalance + oldReceiverBalance + oldSenderBalance <= totalSupply);
   transfer(receiver, amount);
   assert(balances[msg.sender] == oldSenderBalance);
   assert(balances[receiver] == oldReceiverBalance);
   assert(balances[owner] == oldOwnerBalance);
}