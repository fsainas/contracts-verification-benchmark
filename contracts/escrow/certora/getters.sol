function getBalance() public view returns (uint256) {
    return address(this).balance;
}

function getBuyer() public view returns (address) {
    return buyer;
}

function getSeller() public view returns (address) {
    return seller;
}

function getArbiter() public view returns (address) {
    return arbiter;
}

function getState() public view returns (Escrow.State) {
    return state;
}