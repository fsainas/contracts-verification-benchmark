methods {
    function deposit() external;
    function win(address) external;
    function timeout() external;
    
    function getBalance() external returns (int) envfree;
    function getBalanceA() external returns (int) envfree;
    function getBalanceB() external returns (int) envfree;    
}
