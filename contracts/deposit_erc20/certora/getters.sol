function getBalance() public view returns (uint) {
    return token.balanceOf(address(this));
}

function getAddressBalance(address addr) public view returns (uint) {
    return token.balanceOf(addr);
}

function getSent() public view returns (uint) {
    return sent;
}

function getInitialDeposit() public view returns (uint) {
    return initial_deposit;
}
