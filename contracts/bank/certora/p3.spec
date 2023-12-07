rule P3 {
    env e;
    calldataarg args;
    method f;

    uint amount;
    
    uint balanceBefore = getContractBalance();
    f(e, args);
    uint balanceAfter = getContractBalance();
    
    assert balanceBefore > balanceAfter => f.selector == sig:withdraw(uint).selector;
}
