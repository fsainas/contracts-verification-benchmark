rule wd_fin_before {
    env e1;
    
    address addr;
    uint amt;
    withdraw(e1, addr, amt);

    env e2;
    require (to_mathint(e2.block.number) < to_mathint(e1.block.number) + to_mathint(currentContract.wait_time));
    finalize@withrevert(e2);

    assert lastReverted;
}
