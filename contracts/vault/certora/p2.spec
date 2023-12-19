rule P2 {
    env e;

    cancel@withrevert(e);
    
    assert(!lastReverted => e.msg.sender == getRecovery());
}
