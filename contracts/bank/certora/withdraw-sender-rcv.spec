// SPDX-License-Identifier: GPL-3.0-only

rule withdraw_sender_rcv {
    env e;
    uint256 amount;

    mathint old_user_balance = currentContract.balanceOf(e.msg.sender);
    withdraw(e,amount);
    mathint new_user_balance = currentContract.balanceOf(e.msg.sender);

    assert new_user_balance == old_user_balance + to_mathint(amount);
}
