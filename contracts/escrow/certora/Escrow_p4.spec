methods {
    function getPhase() external returns (Escrow.Phase) envfree;
}

rule P4 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();
    
    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 == Escrow.Phase.END => (
        p1 == Escrow.Phase.REDEEM ||
        p1 == Escrow.Phase.ARBITR ||
        p1 == Escrow.Phase.CHOOSE
        );
}

rule NotP4 {
    env e;
    method f;
    calldataarg args;
    
    Escrow.Phase p1 = getPhase();
    f(e, args);
    Escrow.Phase p2 = getPhase();

    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    
    assert p2 != Escrow.Phase.END => (
        p1 == Escrow.Phase.REDEEM ||
        p1 == Escrow.Phase.ARBITR ||
        p1 == Escrow.Phase.CHOOSE
        );
}


// V1 proof: 