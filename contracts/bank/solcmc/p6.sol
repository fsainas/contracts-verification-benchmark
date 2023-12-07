function invariant(uint amount) public {
    uint _senderBalanceBefore = balances[msg.sender];
    withdraw(amount);
    assert(amount <= _senderBalanceBefore);
}
