methods {
    function balanceOf(address account) external returns (uint256) envfree;
    function calculateFee(uint256 amount) external returns (uint256) envfree;
}

hook Sstore SimplifiedDeflationaryToken.owner address hook_owner (address hook_old_owner) {
    old_owner = hook_old_owner;
}

ghost address old_owner;

rule ownership_cannot_change {
    env e;
    calldataarg args;

    require(old_owner == currentContract.owner);

    transfer@withrevert(e, args);
    assert(old_owner == currentContract.owner);
    excludeFromFee@withrevert(e, args);
    assert(old_owner == currentContract.owner);
    includeInFee@withrevert(e, args);
    assert(old_owner == currentContract.owner);
}