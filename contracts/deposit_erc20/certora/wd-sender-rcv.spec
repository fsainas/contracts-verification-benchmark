// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule wd_sender_rcv {
    env e;
    uint amount;
    address sender = e.msg.sender;

    mathint before = currentContract.token.balanceOf(e, sender);
    withdraw(e, amount);
    mathint after = currentContract.token.balanceOf(e, sender);

    if(e.msg.sender != currentContract)
        assert after == before + amount;
    else
        assert after == before;
}
