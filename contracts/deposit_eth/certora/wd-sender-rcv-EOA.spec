// SPDX-License-Identifier: GPL-3.0-only

rule wd_sender_rcv_EOA {
    env e;
    uint amount;
    address sender = e.msg.sender;

    require (sender == e.tx.origin);

    mathint before = getAddressBalance(sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(sender);

    assert after == before + amount;
}
