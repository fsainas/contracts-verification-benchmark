methods {
    function withdraw(address, uint) external;
    function finalize() external;
    function getOwner() external returns (address) envfree;
    function getState() external returns (Vault.States) envfree;
}

rule P3 {
    env e;
    calldataarg args;
    method f;
    
    require f.isFallback == false;
    
    Vault.States state1 = getState();
    f(e, args);
    Vault.States state2 = getState();

    require(f.selector != sig:getOwner().selector);
    require(f.selector != sig:getState().selector);
    require(f.selector != sig:getRecovery().selector);

    assert state1 == Vault.States.IDLE => state2 == Vault.States.REQ;
}

rule NotP3 {
    env e;
    calldataarg args;
    method f;
    
    require f.isFallback == false;
    
    Vault.States state1 = getState();
    f(e, args);
    Vault.States state2 = getState();

    require(f.selector != sig:getOwner().selector);
    require(f.selector != sig:getState().selector);
    require(f.selector != sig:getRecovery().selector);

    assert state1 == Vault.States.IDLE => state2 != Vault.States.REQ;
}

// V1 proof: https://prover.certora.com/output/49230/065149d9dab34f778a95b7be8af8aa1c?anonymousKey=43e6acf69bab7f1c2f932da813592224252b4069
// V2 proof: https://prover.certora.com/output/49230/f16e5d783d1a4b91afb4d21e88056280?anonymousKey=bd8d65056cd827cc1f213b9f558e0c237cd41c3d
// V3 proof: https://prover.certora.com/output/49230/5937881dbfeb4aba9190f884ff62c4b4?anonymousKey=43349bd02bbc06abda9a1a7a725bc6a0bae542d6