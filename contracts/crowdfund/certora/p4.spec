rule P4 {
    env e;
    calldataarg args;
    method f;
    
    require(e.block.number > getEndDonate());
    
    mathint before = getBalance();

    f(e, args);

    mathint after = getBalance();
    
    assert before > after => (
        f.selector == sig:withdraw().selector ||
        f.selector == sig:reclaim().selector
    );

    
}

