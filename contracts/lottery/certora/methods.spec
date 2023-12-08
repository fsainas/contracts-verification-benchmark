methods {
    function enter() external;
    function getLastPlayer() external returns (address) envfree;
    function getPlayersLength() external returns (uint) envfree;
    function pickWinner() external;
}
