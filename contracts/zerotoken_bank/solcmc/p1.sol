function invariant(uint amount) public {
    uint currb = balances[msg.sender];

    deposit(amount);

    uint newb = balances[msg.sender];

    assert(newb == currb + amount);
}
