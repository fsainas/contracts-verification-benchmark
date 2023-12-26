methods {
    function getBalance() external returns (uint) envfree;
    function getOwner() external returns (address) envfree;
    function getRecovery() external returns (address) envfree;
    function getWaitTime() external returns (uint) envfree;
    function getReceiver() external returns (address) envfree;
    function getRequestTime() external returns (uint) envfree;
    function getAmount() external returns (uint) envfree;
    function getState() external returns (Vault.States) envfree;
    function receive() external;
    function withdraw(address, uint) external;
    function finalize() external;
    function cancel() external;
}
