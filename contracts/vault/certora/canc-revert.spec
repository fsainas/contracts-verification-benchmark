rule canc_revert {
    env e;

    cancel@withrevert(e);
    
    assert(!lastReverted => e.msg.sender == currentContract.recovery);
}
