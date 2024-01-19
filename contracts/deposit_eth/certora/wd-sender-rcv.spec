// SPDX-License-Identifier: GPL-3.0-only

rule wd_sender_rcv {
    env e;
    uint amount;
    address sender = e.msg.sender;

    mathint before = getAddressBalance(sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(sender);

    assert after == before + amount;
}
