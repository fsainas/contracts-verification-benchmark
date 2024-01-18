// SPDX-License-Identifier: GPL-3.0-only

rule user_balance_inc_onlyif_deposit {
    env e;
    method f;
    calldataarg args;
    address a;

    mathint currb = getBalanceEntry(a);
    f(e, args);
    mathint newb = getBalanceEntry(a);

    assert(newb > currb => (f.selector == sig:deposit().selector && e.msg.sender == a));
}
