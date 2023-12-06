methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
    function releasable(address) external returns(uint) envfree;
    function getBalance() external returns(uint) envfree;
    function getTotalReleasable() external returns(uint) envfree;
}
