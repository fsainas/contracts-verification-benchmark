function invariant(uint amount) public {
    require (amount == 0 || amount > balances[msg.sender]);
    withdraw(amount);
    assert(false);
}
