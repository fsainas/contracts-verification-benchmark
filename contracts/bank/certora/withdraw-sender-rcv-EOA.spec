// SPDX-License-Identifier: GPL-3.0-only

rule withdraw_sender_rcv_EOA {
    env e;
    uint256 amount;

    address sender = e.msg.sender;
    require (sender == e.tx.origin);

    mathint old_user_balance = getAddressBalance(sender);

    withdraw(e,amount);

    mathint new_user_balance = getAddressBalance(sender);

    mathint amount_mathint = to_mathint(amount);
    assert new_user_balance == old_user_balance + amount_mathint;
}