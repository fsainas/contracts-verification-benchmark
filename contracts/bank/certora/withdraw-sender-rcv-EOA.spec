// SPDX-License-Identifier: GPL-3.0-only

rule withdraw_sender_rcv_EOA {
    env e;
    uint256 amount;

    require (e.msg.sender == e.tx.origin);

    mathint old_user_balance = currentContract.balanceOf(e.msg.sender);
    withdraw(e,amount);
    mathint new_user_balance = currentContract.balanceOf(e.msg.sender);

    assert new_user_balance == old_user_balance + to_mathint(amount);
}
