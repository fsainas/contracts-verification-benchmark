function ownerFeeAfterTransfer(uint256 amount) public view {
   require(amount > 0);
   require(isExcludedFromFee[msg.sender] == false);
   uint256 fee = calculateFee(amount);
   assert(fee > 0);
}