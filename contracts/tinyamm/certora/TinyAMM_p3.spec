methods {
       function getEverDeposited() external returns (bool);
       function getSupply() external returns (uint) envfree;
       function getR0() external returns (uint);
       function getR1() external returns (uint);
       function swap(address, uint, uint) external;
}

rule P3 {
    env e;
    calldataarg args;
    method f;
    
    mathint supply_before = getSupply();
    f(e, args);
    mathint supply_after = getSupply();

    assert f.selector != sig:swap(address, uint, uint).selector =>
        supply_after == supply_before;
}

rule NotP3 {
    env e;
    calldataarg args;
    method f;
    
    mathint supply_before = getSupply();
    f(e, args);
    mathint supply_after = getSupply();

    assert f.selector != sig:swap(address, uint, uint).selector =>
        supply_after != supply_before;
}

// V1 proof: https://prover.certora.com/output/49230/d7ef86ff8ad84459adad3ea88831829d?anonymousKey=7619c1b2ea6402f9144a46151bd0601a70897c13