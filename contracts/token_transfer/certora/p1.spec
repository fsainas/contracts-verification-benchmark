rule P1 {
    env e;
    method f;
    calldataarg args;

    deposit(e);
    f(e, args);
    
    assert f.selector != sig:deposit().selector;
}

