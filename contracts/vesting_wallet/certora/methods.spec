methods {
    function receive() external;
    function releasable() external returns (uint256);
    function release() external;  
    function getBalance() external returns (uint256) envfree;
    function getBeneficiaryBalance() external returns (uint256) envfree;
    function getStart() external returns (uint64) envfree;
    function getDuration() external returns (uint64) envfree;
    function vestedAmount(uint64) external returns (uint256) envfree;
}