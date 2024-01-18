methods {
    function getBalanceEntry(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns(uint) envfree;
    function withdraw(uint) external;
}

