function getBalanceEntry(address a) public view returns (uint) {
    return balances[a];
}

function getContractBalance() public view returns (uint) {
    return address(this).balance;
}

function getAddressBalance(address a) public view returns (uint) {
    return a.balance;
}

function getContractAddress() public view returns (address) {
    return address(this);
}
