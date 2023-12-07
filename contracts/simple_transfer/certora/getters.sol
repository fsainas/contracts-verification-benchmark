function getBalance() public view returns (uint) {
    return address(this).balance;
}

function getAddressBalance(address addr) public view returns (uint) {
    return addr.balance;
}
