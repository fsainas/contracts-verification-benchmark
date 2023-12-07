function invariant() public payable {
    require(address(this).balance - msg.value >= balances[msg.sender]);
    deposit();
    assert(address(this).balance >= balances[msg.sender]);
}
