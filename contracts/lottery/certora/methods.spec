methods {
    function enter() external;
    function getLastPlayer() external returns (address) envfree;
    function getPlayersLength() external returns (uint) envfree;
    function pickWinner() external;
    function balanceOf(address) external returns (uint) envfree;
}
