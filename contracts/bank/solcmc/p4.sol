function invariant(uint amount) public {
    uint _senderBalanceBefore = balances[msg.sender];
    withdraw(amount);
    uint _senderBalanceAfter = balances[msg.sender];
    assert(_senderBalanceBefore == _senderBalanceAfter + amount);
}
