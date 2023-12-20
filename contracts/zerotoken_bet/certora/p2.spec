// P2: the contract balance does not exceed 2 tokens

invariant nonneg_and_sum2()
    // getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    // getBalanceA() + getBalanceB() + getBalance() == 2;
    currentContract.balance_a>=0 && currentContract.balance_b>=0 && currentContract.balance>=0 &&
    currentContract.balance_a + currentContract.balance_b + currentContract.balance == 2;

rule P2 {
    requireInvariant nonneg_and_sum2();

    method f;
    env e;
    calldataarg args;

    // f is an arbitrary method of OracleBet
    require
        f.selector == sig:deposit().selector
     || f.selector == sig:win(address).selector
     || f.selector == sig:timeout().selector;

    // executes method f in any state 
    f(e,args);

    // assert that the contract balance does not exceed 2 tokens
    mathint b = currentContract.balance;
    assert b <= 2;
}
