ghost mathint sent;

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    sent = sent + value;
}

rule arbitrate_send {
    require sent == 0;

    env e;
    address a;
    arbitrate(e, a);

    assert sent == to_mathint(getFee());
}
