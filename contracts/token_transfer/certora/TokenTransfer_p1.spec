methods {
}

rule P1 {
    env e;
    method f;
    calldataarg args;

    deposit(e);
    f(e, args);
    
    assert f.selector != sig:deposit().selector;
}

rule NotP1 {
    env e;
    method f;
    calldataarg args;

    deposit(e);
    f(e, args);
    
    assert f.selector == sig:deposit().selector;
}

// V1 proof: https://prover.certora.com/output/49230/307fd1ba71b84e43b7a76dfa6552a60a?anonymousKey=d478fd50e1304747bd4e568bd9513b31384ec404
// V2 proof: https://prover.certora.com/output/49230/da32523edc314a4595886d66adb46923?anonymousKey=448dbd90994b034d803a6db3bd10783d1e00a013