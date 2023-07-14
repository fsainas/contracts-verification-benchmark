methods {
    function getPhase() external returns (Escrow.Phase) envfree;
    function getEscrowChoice() external returns (address) envfree;
    function getBalance() external returns (uint) envfree;
}

rule P5 {
    env e;
    method f;
    calldataarg args;
    
    uint balance_before = getBalance();
    f(e, args);
    uint balance_after = getBalance();

    Escrow.Phase p = getPhase();

    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    require f.selector != sig:getEscrowChoice().selector;
    require f.selector != sig:getBalance().selector;
    require f.selector != sig:getBuyer().selector;
    require f.selector != sig:getSeller().selector;
    require f.selector != sig:getEscrow().selector;
    
    assert p == Escrow.Phase.END && getEscrowChoice() != 0 => (
        f.selector == sig:redeem_arbitrated().selector &&
        balance_before != balance_after
        );
}

rule NotP5 {
    env e;
    method f;
    calldataarg args;
    
    uint balance_before = getBalance();
    f(e, args);
    uint balance_after = getBalance();

    Escrow.Phase p = getPhase();

    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    require f.selector != sig:getEscrowChoice().selector;
    require f.selector != sig:getBalance().selector;
    require f.selector != sig:getBuyer().selector;
    require f.selector != sig:getSeller().selector;
    require f.selector != sig:getEscrow().selector;
    
    assert p != Escrow.Phase.END && getEscrowChoice() != 0 => (
        f.selector == sig:redeem_arbitrated().selector &&
        balance_before != balance_after
        );
}


// V1 proof:  