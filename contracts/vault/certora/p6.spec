rule P6 {
    env e1;
    
    address addr;
    uint amt;
    withdraw(e1, addr, amt);

    env e2;
    require (e2.block.number < assert_uint256(e1.block.number + currentContract.wait_time));
    finalize(e2);

    satisfy !lastReverted;
}
