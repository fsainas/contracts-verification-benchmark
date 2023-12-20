// if the last transaction was not a swap the supply has not changed

rule P3 {
    env e;
    calldataarg args;
    method f;
    
    mathint supply_before = currentContract.supply;
    f(e, args);
    mathint supply_after = currentContract.supply;

    assert f.selector != sig:swap(address, uint, uint).selector =>
        supply_after == supply_before;
}
