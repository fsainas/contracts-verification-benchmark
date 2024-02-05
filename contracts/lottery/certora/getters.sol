function getLastPlayer() public view returns (address) {
    return players[players.length-1];
}

function getPlayersLength() public view returns (uint) {
    return players.length;
}

function balanceOf(address a) public view returns (uint) {
    return a.balance;
}
