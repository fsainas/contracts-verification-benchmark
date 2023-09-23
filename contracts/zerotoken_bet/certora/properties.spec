methods {
    function deposit() external;
    function win(address) external;
    function timeout() external;
    
    function getBalance() external returns (int) envfree;
    function getBalanceA() external returns (int) envfree;
    function getBalanceB() external returns (int) envfree;    
}

invariant nonneg_and_sum2()
    getBalanceA()>=0 && getBalanceB()>=0 && getBalance()>=0 &&
    getBalanceA() + getBalanceB() + getBalance() == 2;

rule P1 {
    requireInvariant nonneg_and_sum2();
    assert true;
}

rule P2 {
    requireInvariant nonneg_and_sum2();

    method f;
    env e;
    calldataarg args;

    require f.selector == sig:deposit().selector
     || f.selector == sig:win(address).selector    
     || f.selector == sig:timeout().selector;
    
    f(e,args);    

    mathint b = getBalance();        
    assert b <= 2;    
}
