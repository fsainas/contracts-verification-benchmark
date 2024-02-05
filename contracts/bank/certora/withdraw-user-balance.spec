// SPDX-License-Identifier: GPL-3.0-only

rule withdraw_user_balance {
    env e;
    uint256 amount;

    mathint old_user_balance = currentContract.balances[e.msg.sender];
    withdraw(e,amount);
    mathint new_user_balance = currentContract.balances[e.msg.sender];

    assert new_user_balance == old_user_balance - to_mathint(amount);
}
