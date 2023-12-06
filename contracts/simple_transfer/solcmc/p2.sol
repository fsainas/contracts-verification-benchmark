function invariant(uint amount) public {
    uint _prev_balance = address(this).balance;	
    withdraw(amount);
    assert(address(this).balance == _prev_balance - amount);
}
