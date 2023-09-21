methods {
    function deposit() external;
    function win(address) external;
    function timeout() external;
    
    function getBalance() external returns (uint) envfree;
    function getBalanceA() external returns (uint) envfree;
    function getBalanceB() external returns (uint) envfree;    
}

rule P1 {
    env e;

    mathint before = getBalance();
    deposit(e);
    mathint after = getBalance();

    assert after <= 0;
}
