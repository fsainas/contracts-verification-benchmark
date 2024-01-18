    
rule candep {

    env e;
    mathint old_balance_b = getBalanceB();
    mathint old_balance = getBalance();

    require e.block.number <= getTimeoutBlock();
    require old_balance_b>=1 && old_balance==1;

    //deposit(e);
    deposit@withrevert(e);

    bool depositReverted = lastReverted;

    mathint new_balance_b = getBalanceB();
    mathint new_balance = getBalance();

    assert !depositReverted => (new_balance_b==old_balance_b-1 && new_balance==2);

}

