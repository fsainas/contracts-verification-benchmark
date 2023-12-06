rule P6 {
    env e;
    method f;
    calldataarg args;
    
    require e.block.number > getEndDonate();
    require getBalance() >= getGoal();
    mathint balance_before = getBalance();
    f(e, args);
    mathint balance_after = getBalance();
    
    assert balance_before > balance_after => (
        f.selector == sig:withdraw().selector &&
        e.msg.sender == getReceiver()
        );
}


