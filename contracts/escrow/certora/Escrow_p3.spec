methods {
    function getPhase() external returns (Escrow.Phase) envfree;
}

rule P3 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();
    
    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 == Escrow.Phase.ARBITR => p1 == Escrow.Phase.REDEEM;
}

rule NotP3 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();

    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 == Escrow.Phase.ARBITR => p1 != Escrow.Phase.REDEEM;
}


// V1 proof:  https://prover.certora.com/output/49230/4921364c27ef496481a0544e9683dfd0?anonymousKey=3a42801adafbd1d954d1c83ad4445e3415ff7e17