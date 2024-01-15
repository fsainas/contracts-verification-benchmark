rule deposit_user_balance {
    env e;

    address sender = e.msg.sender;
    mathint old_user_balance = getBalance(sender);

    deposit(e);

    mathint new_user_balance = getBalance(sender);

    mathint deposit_amount = to_mathint(e.msg.value);
    assert new_user_balance == old_user_balance + deposit_amount;
}
