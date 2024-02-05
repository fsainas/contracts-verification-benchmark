// SPDX-License-Identifier: GPL-3.0-only

rule user_balance_dec_onlyif_withdraw {
    env e;
    method f;
    calldataarg args;
    address a;

    mathint currb = currentContract.balances[a];
    f(e, args);
    mathint newb = currentContract.balances[a];

    assert (newb < currb => (f.selector == sig:withdraw(uint).selector && e.msg.sender == a));
}
