methods {
    function approve_payment() external;
    function refund() external; 
    function open_dispute() external;
    function arbitrate(address) external;
    function redeem() external;
    function getBalance() external returns (uint256) envfree;
    function getBuyer() external returns (address) envfree;
    function getSeller() external returns (address) envfree;
    function getArbiter() external returns (address) envfree;
    function getState() external returns (Escrow.State) envfree;
}