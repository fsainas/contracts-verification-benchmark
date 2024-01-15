rule user_balance_dec_onlyif_withdraw {
    env e;
    method f;
    calldataarg args;
    address a;

    mathint currb = getBalance(a);
    f(e, args);
    mathint newb = getBalance(a);

    assert (newb < currb => (f.selector == sig:withdraw(uint).selector && e.msg.sender == a));
}