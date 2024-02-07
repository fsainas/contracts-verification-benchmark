function invariant(uint amount) public {
    uint old_balance = token.balanceOf(address(this));	

    withdraw(amount);

    uint new_balance = token.balanceOf(address(this));

    assert(new_balance == old_balance - amount);
}
