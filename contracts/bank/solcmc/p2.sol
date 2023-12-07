function invariant() public payable {
    uint _balanceBefore = balances[msg.sender];
    deposit();
    uint _balanceAfter = balances[msg.sender];
    assert(!(msg.value > 0) || _balanceBefore < _balanceAfter);
}
