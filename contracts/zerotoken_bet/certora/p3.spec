invariant nonneg_and_sum2()
    getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    getBalanceA() + getBalanceB() + getBalance() == 2;

rule P3 {
    requireInvariant nonneg_and_sum2();
    mathint old_balance_b = getBalanceB();
    mathint old_balance = getBalance();    
    env e;

    require (old_balance_b>=1 && old_balance==1);
    deposit@withrevert(e);

    bool depositReverted = lastReverted;
    
    mathint new_balance_b = getBalanceB();
    mathint new_balance = getBalance();    
    assert !depositReverted => (new_balance_b==old_balance_b-1 && new_balance==2);    
}
