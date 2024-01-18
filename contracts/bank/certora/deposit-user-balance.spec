// SPDX-License-Identifier: GPL-3.0-only

rule deposit_user_balance {
    env e;

    address sender = e.msg.sender;
    mathint old_user_balance = getBalanceEntry(sender);

    deposit(e);

    mathint new_user_balance = getBalanceEntry(sender);

    mathint deposit_amount = to_mathint(e.msg.value);
    assert new_user_balance == old_user_balance + deposit_amount;
}
