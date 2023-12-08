function getLastPlayer() public view returns (address) {
    return players[players.length-1];
}

function getPlayersLength() public view returns (uint) {
    return players.length;
}
