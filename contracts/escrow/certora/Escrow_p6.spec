methods {
    function getPhase() external returns (Escrow.Phase) envfree;
    function getEscrowChoice() external returns (address) envfree;
    function getBalance() external returns (uint) envfree;
    function getBuyer() external returns (address) envfree;
    function getSeller() external returns (address) envfree;
    function getEscrow() external returns (address) envfree;
}

rule P6 {
    env e;
    method f;
    calldataarg args;
    
    f(e, args);
    
    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    require f.selector != sig:getEscrowChoice().selector;
    require f.selector != sig:getBalance().selector;
    require f.selector != sig:getBuyer().selector;
    require f.selector != sig:getSeller().selector;
    require f.selector != sig:getEscrow().selector;
    require f.selector != sig:redeem_arbitrated().selector;
    require f.selector != sig:choose(address).selector;

    assert e.msg.sender == getBuyer() || e.msg.sender == getSeller() || e.msg.sender == getEscrow();
}

rule NotP6 {
    env e;
    method f;
    calldataarg args;
    
    f(e, args);
    
    require f.selector != sig:getFee().selector;
    require f.selector != sig:getPhase().selector;
    require f.selector != sig:getEscrowChoice().selector;
    require f.selector != sig:getBalance().selector;
    require f.selector != sig:getBuyer().selector;
    require f.selector != sig:getSeller().selector;
    require f.selector != sig:getEscrow().selector;
    require f.selector != sig:redeem_arbitrated().selector;
    require f.selector != sig:choose(address).selector;

    assert e.msg.sender != getBuyer() || e.msg.sender != getSeller() || e.msg.sender != getEscrow();
}


// V1 proof: https://prover.certora.com/output/49230/06eaee7860f34df496310365fbd6f1ec?anonymousKey=79042e72bd8bd3d27a863551b884ed45c7796062