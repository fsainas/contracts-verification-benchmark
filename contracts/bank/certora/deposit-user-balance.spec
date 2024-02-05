// SPDX-License-Identifier: GPL-3.0-only

rule deposit_user_balance {
    env e;

    mathint old_user_balance = currentContract.balances[e.msg.sender];
    deposit(e);
    mathint new_user_balance = currentContract.balances[e.msg.sender];

    assert new_user_balance == old_user_balance + to_mathint(e.msg.value);
}
