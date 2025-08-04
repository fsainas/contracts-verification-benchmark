methods {
   function balanceOf(address account) external returns (uint256) envfree;
   function calculateFee(uint256 amount) external returns (uint256) envfree;
}

rule validate_transfer_same_o_r {
   env e;
   address owner = currentContract.owner;
   address receiver;

   uint256 amount;
   uint256 expectedFee = currentContract.isExcludedFromFee[e.msg.sender] ? 0
                                                   : calculateFee(amount);

   requireInvariant correctTotalSupply;
   requireInvariant correctTransactionFeePercent;

   require(owner == receiver && e.msg.sender != receiver);

   mathint oldOwnerBalance = balanceOf(owner);
   mathint oldSenderBalance = balanceOf(e.msg.sender);
   mathint oldReceiverBalance = balanceOf(receiver);
   require(oldOwnerBalance + oldReceiverBalance + oldSenderBalance <= currentContract.totalSupply);

   transfer(e, receiver, amount);

   assert(balanceOf(owner) == oldOwnerBalance + amount);
   assert(balanceOf(e.msg.sender) == oldSenderBalance - amount);
   assert(balanceOf(receiver) == oldReceiverBalance + amount);
}

invariant correctTransactionFeePercent()
   currentContract.transactionFeePercent == 10;

invariant correctTotalSupply()
   currentContract.totalSupply == 1000000000000000000000000;