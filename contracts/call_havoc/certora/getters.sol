function getBalance() public view returns (uint) {
    return address(this).balance;
}

function getX() public view returns (uint) {
    return x;
}
