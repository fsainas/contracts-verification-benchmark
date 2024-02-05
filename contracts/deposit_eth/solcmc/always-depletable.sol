function invariant() public {
    require(msg.sender == tx.origin);
    uint amount = address(this).balance;
    withdraw(amount);
    assert(address(this).balance == 0);
}
