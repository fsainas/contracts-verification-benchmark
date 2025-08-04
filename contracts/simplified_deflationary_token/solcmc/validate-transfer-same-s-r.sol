function validateTransferSR(address receiver, uint256 amount) public {
   require(owner != msg.sender && msg.sender == receiver);
   uint256 oldSenderBalance = balances[msg.sender];
   uint256 oldReceiverBalance = balances[receiver];
   uint256 oldOwnerBalance = balances[owner];
   uint256 expectedFee = isExcludedFromFee[msg.sender] ? 0 : calculateFee(amount);

   require(oldOwnerBalance + oldReceiverBalance + oldSenderBalance <= totalSupply);
   transfer(receiver, amount);
   assert(balances[msg.sender] == oldSenderBalance - expectedFee);
   assert(balances[receiver] == oldReceiverBalance - expectedFee);
   assert(balances[owner] == oldOwnerBalance + expectedFee);
}

