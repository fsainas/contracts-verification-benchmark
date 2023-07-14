methods {
    function getPhase() external returns (Escrow.Phase) envfree;
}

rule P2 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();
    
    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 == Escrow.Phase.REDEEM => p1 == Escrow.Phase.CHOOSE;
}

rule NotP2 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();

    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 == Escrow.Phase.REDEEM => p1 != Escrow.Phase.CHOOSE;
}


// V1 proof: https://prover.certora.com/output/49230/7d71cbed8cfd4c2cb3e2da26c30cb71b?anonymousKey=fb28cc6d3818afc4d5fd6f276f4b8104110e8058