rule P5 {
    env e;
    method f;
    calldataarg args;
    address a;

    uint currb = balanceOf(a);
    f(e, args);
    uint newb = balanceOf(a);

    assert(newb < currb => (f.selector == sig:withdraw(uint).selector && e.msg.sender == a));
}
