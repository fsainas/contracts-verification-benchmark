// P4: if B has less than 1 token or he has already joined the bet yet, then he cannot deposit 1 token in the contract
   
invariant nonneg_and_sum2()
    // getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    // getBalanceA() + getBalanceB() + getBalance() == 2;
    currentContract.balance_a>=0 && currentContract.balance_b>=0 && currentContract.balance>=0 &&
    currentContract.balance_a + currentContract.balance_b + currentContract.balance == 2;    

rule P4 {
    requireInvariant nonneg_and_sum2();
    mathint old_balance_b = currentContract.balance_b;
    mathint old_balance = currentContract.balance;    
    env e;

    require (old_balance_b<1 || old_balance!=1);
    deposit@withrevert(e);
    assert (lastReverted);
}
