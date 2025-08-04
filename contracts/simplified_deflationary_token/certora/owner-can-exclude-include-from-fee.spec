rule owner_can_exclude_include_from_fee {
    env e;
    address owner = currentContract.owner;
    address account;

    require(owner == e.msg.sender);
    require(e.msg.value == 0);
    require(currentContract.isExcludedFromFee[account] == false);
    excludeFromFee@withrevert(e, account);
    assert(currentContract.isExcludedFromFee[account] == true);
    includeInFee@withrevert(e, account);
    assert(currentContract.isExcludedFromFee[account] == false);
}