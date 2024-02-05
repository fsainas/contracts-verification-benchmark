methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getDonated(address) external returns(uint) envfree;
    function balanceOf(address) external returns(uint) envfree;
    function getGoal() external returns (uint) envfree;
    function getOwner() external returns (address) envfree;
    function withdraw() external;
    function reclaim() external;
}
