rule P4 {
    env e;
    calldataarg args;
    method f;
    
    require(e.block.number > getEndDonate());
    
    mathint old_balance = getBalance();

    f(e, args);

    mathint new_balance = getBalance();
    
    assert old_balance > new_balance => (
        f.selector == sig:withdraw().selector ||
        f.selector == sig:reclaim().selector
    );

    
}

