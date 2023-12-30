function invariant(uint amount) public {
    uint prev_balance = address(this).balance;	
    withdraw(amount);
    assert(address(this).balance == prev_balance - amount);
}
