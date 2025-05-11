ghost bool external_call;

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    external_call = true;
}

rule ex_call_is_made {
    require !external_call;

    env e; 
    address a;
    f(e, a);

    assert external_call;
}