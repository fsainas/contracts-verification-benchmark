function ownerCanExcludeIncludeFromFee(address user) public {
    require(owner == msg.sender);
    require(isExcludedFromFee[user] == false);
    excludeFromFee(user);
    assert(isExcludedFromFee[user] == true);
    includeInFee(user);
    assert(isExcludedFromFee[user] == false);
}