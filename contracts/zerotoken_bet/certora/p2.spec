// P2: the contract balance does not exceed 2 tokens

invariant nonneg_and_sum2()
    getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    getBalanceA() + getBalanceB() + getBalance() == 2;

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
    mathint b = getBalance();
    assert b <= 2;
}
