methods {
    function deposit() external;
    function win(address) external;
    function timeout() external;
    
    function getBalance() external returns (int) envfree;
    function getBalanceA() external returns (int) envfree;
    function getBalanceB() external returns (int) envfree;    
}

invariant sum2()
    getBalanceA() + getBalanceB() + getBalance() == 2;

rule P1 {
    env e1;    
    deposit(e1);
    mathint b1 = getBalance();    
    assert b1 >= 0;

    env e2;
    address p;
    win(e2, p);
    mathint b2 = getBalance();    
    assert b2 >= 0;

    env e3;    
    timeout(e3);
    mathint b3 = getBalance();    
    assert b3 >= 0;    
}

rule P2 {
    requireInvariant sum2();
    
    env e1;    
    deposit(e1);
    mathint b1 = getBalance();    
    assert b1 <= 2;

    env e2;
    address p;
    win(e2, p);
    mathint b2 = getBalance();    
    assert b2 <= 2;

    env e3;    
    timeout(e3);
    mathint b3 = getBalance();    
    assert b3 <= 2;    
}
