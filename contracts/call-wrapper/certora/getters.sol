function getBalance() public view returns (uint) {
    return address(this).balance;
}

function getData() public view returns (uint) {
    return data;
}