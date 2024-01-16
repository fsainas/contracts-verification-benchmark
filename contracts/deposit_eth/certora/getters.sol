function getBalance() public view returns (uint) {
    return address(this).balance;
}

function getAddressBalance(address addr) public view returns (uint) {
    return addr.balance;
}

function getSent() public view returns (uint) {
    return sent;
}

function getInitialDeposit() public view returns (uint) {
    return initial_deposit;
}
