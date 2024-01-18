    
rule cannotdep {
    env e;
    mathint old_balance_b = currentContract.balance_b;
    mathint old_balance = currentContract.balance;    

    require (old_balance_b<1 || old_balance!=1);
    deposit@withrevert(e);
    assert (lastReverted);

    require (old_balance_b<1 || old_balance!=1);
    deposit@withrevert(e);
    assert (lastReverted);
}

