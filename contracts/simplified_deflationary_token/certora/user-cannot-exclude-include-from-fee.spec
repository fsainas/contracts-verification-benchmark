rule user_cannot_exclude_include_from_fee {
    env e;
    address owner = currentContract.owner;
    address account;

    require(owner != e.msg.sender);
    require(e.msg.value == 0);

    require(currentContract.isExcludedFromFee[account] == false);
    excludeFromFee@withrevert(e, account);
    assert(currentContract.isExcludedFromFee[account] == false);

    require(currentContract.isExcludedFromFee[e.msg.sender] == true);
    includeInFee@withrevert(e, e.msg.sender);
    assert(currentContract.isExcludedFromFee[e.msg.sender] == true);
}