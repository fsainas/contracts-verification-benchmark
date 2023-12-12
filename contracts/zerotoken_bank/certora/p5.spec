rule P5 {
    env e;
    method f;
    calldataarg args;
    address a;

    uint currb = balanceOf(a);
    f(e, args);
    uint newb = balanceOf(a);

    assert(newb > currb => (f.selector == sig:deposit(uint).selector && e.msg.sender == a));
}
