function validateTransferSameOR(address receiver, uint256 amount) public {
   require(owner != msg.sender && owner == receiver);
   uint256 oldSenderBalance = balances[msg.sender];
   uint256 oldReceiverBalance = balances[receiver];
   uint256 oldOwnerBalance = balances[owner];
   require(oldOwnerBalance + oldReceiverBalance + oldSenderBalance <= totalSupply);
   transfer(receiver, amount);
   assert(balances[msg.sender] == oldSenderBalance - amount);
   assert(balances[receiver] == oldReceiverBalance + amount);
   assert(balances[owner] == oldOwnerBalance + amount);
}