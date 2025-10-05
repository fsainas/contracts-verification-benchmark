function userCannotExcludeIncludeFromFee(address user) public {
   require(owner != msg.sender);
   require(isExcludedFromFee[user] == false);
   excludeFromFee(user);
   assert(isExcludedFromFee[user] == false);
   require(isExcludedFromFee[msg.sender] == true);
   includeInFee(msg.sender);
   assert(isExcludedFromFee[msg.sender] == true);
}