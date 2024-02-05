function invariant(uint amount) public {
    uint old_user_balance = address(msg.sender).balance;
    withdraw(amount);
    uint new_user_balance = address(msg.sender).balance;
    assert(new_user_balance == old_user_balance + amount);
}
