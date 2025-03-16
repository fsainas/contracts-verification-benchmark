// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule wd_sender_rcv {
    env e;
    uint amount;
    address sender = e.msg.sender;

    mathint before = getAddressBalance(e, sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(e, sender);

    if(e.msg.sender != currentContract)
        assert after == before + amount;
    else
        assert after == before;
}
