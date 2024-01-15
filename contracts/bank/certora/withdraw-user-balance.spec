rule withdraw_user_balance {
    env e;
    uint256 amount;

    address sender = e.msg.sender;
    mathint old_user_balance = getBalance(sender);

    withdraw(e,amount);

    mathint new_user_balance = getBalance(sender);

    mathint amount_mathint = to_mathint(amount);
    assert new_user_balance == old_user_balance - amount_mathint;
}
