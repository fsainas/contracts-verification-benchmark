function invariant(uint amount) public {
    uint currb = balances[msg.sender];

    withdraw(amount);

    uint newb = balances[msg.sender];

    assert(newb == currb - amount);
}
