methods {
    function deposit() external;
    function win(address) external;
    function timeout() external;
    
    function getBalance() external returns (uint);
    function getBalanceA() external returns (uint);
    function getBalanceB() external returns (uint);    
}

rule P1 {
    env e1;    
    deposit(e1);
    mathint b1 = getBalance(e1);    
    assert b1 >= 0;

    env e2;
    address p;
    win(e2, p);
    mathint b2 = getBalance(e2);    
    assert b2 >= 0;

    env e3;    
    timeout(e3);
    mathint b3 = getBalance(e3);    
    assert b3 >= 0;    
}

rule P2 {
    env e1;    
    deposit(e1);
    mathint b1 = getBalance(e1);    
    assert b1 <= 2;

    env e2;
    address p;
    win(e2, p);
    mathint b2 = getBalance(e2);    
    assert b2 <= 2;

    env e3;    
    timeout(e3);
    mathint b3 = getBalance(e3);    
    assert b3 <= 2;    
}
