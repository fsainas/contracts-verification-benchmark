// P1: the contract balance is always nonnegative

invariant nonneg_and_sum2()
    // getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    // getBalanceA() + getBalanceB() + getBalance() == 2;
    currentContract.balance_a>=0 && currentContract.balance_b>=0 && currentContract.balance>=0 &&
    currentContract.balance_a + currentContract.balance_b + currentContract.balance == 2;
    
rule P1 {
    requireInvariant nonneg_and_sum2();
    assert true;
}
