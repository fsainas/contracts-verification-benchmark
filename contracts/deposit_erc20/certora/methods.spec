methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns (uint) envfree;
    function getInitialDeposit() external returns (uint) envfree;
    function getSent() external returns (uint) envfree;
}