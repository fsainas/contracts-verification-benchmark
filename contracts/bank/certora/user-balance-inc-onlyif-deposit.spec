rule user_balance_inc_onlyif_deposit {
    env e;
    method f;
    calldataarg args;
    address a;

    mathint currb = getBalance(a);
    f(e, args);
    mathint newb = getBalance(a);

    assert(newb > currb => (f.selector == sig:deposit().selector && e.msg.sender == a));
}
