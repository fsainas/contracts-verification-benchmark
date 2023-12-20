// P3: before the deadline, if B has at least 1 token and he has not joined the bet yet, then he can deposit 1 token in the contract

invariant nonneg_and_sum2()
    // getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    // getBalanceA() + getBalanceB() + getBalance() == 2;
    currentContract.balance_a>=0 && currentContract.balance_b>=0 && currentContract.balance>=0 &&
    currentContract.balance_a + currentContract.balance_b + currentContract.balance == 2;
    

rule P3 {
    requireInvariant nonneg_and_sum2();
    mathint old_balance_b = currentContract.balance_b;
    mathint old_balance = currentContract.balance;    
    env e;

    require (old_balance_b>=1 && old_balance==1);
    deposit@withrevert(e);

    bool depositReverted = lastReverted;
    
    mathint new_balance_b = currentContract.balance_b;
    mathint new_balance = currentContract.balance;    
    assert !depositReverted => (new_balance_b==old_balance_b-1 && new_balance==2);    
}
