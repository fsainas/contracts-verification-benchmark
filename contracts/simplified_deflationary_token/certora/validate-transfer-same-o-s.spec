methods {
   function balanceOf(address account) external returns (uint256) envfree;
   function calculateFee(uint256 amount) external returns (uint256) envfree;
}

rule validate_transfer_same_o_s {
   env e;
   address owner = currentContract.owner;
   address receiver;

   requireInvariant correctTotalSupply;
   requireInvariant correctTransactionFeePercent;

   uint256 amount;
   uint256 expectedFee = currentContract.isExcludedFromFee[e.msg.sender] ? 0
                                                   : calculateFee(amount);
  
   require owner == e.msg.sender && e.msg.sender != receiver;

   mathint oldOwnerBalance = balanceOf(owner);
   mathint oldSenderBalance = balanceOf(e.msg.sender);
   mathint oldReceiverBalance = balanceOf(receiver);
   require (oldOwnerBalance + oldReceiverBalance) == currentContract.totalSupply;

   transfer(e, receiver, amount);
  
   assert(balanceOf(owner) == oldOwnerBalance - amount + expectedFee);
   assert(balanceOf(e.msg.sender) == oldSenderBalance - amount + expectedFee);
   assert(balanceOf(receiver) == oldReceiverBalance + amount - expectedFee);
}

invariant correctTransactionFeePercent()
   currentContract.transactionFeePercent == 10;

invariant correctTotalSupply()
   currentContract.totalSupply == 1000000000000000000000000;