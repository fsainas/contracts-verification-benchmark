function invariant() public payable {
    uint old_user_balance = balances[msg.sender];
    deposit();
    uint new_user_balance = balances[msg.sender];
    assert(new_user_balance == old_user_balance + msg.value);
}
