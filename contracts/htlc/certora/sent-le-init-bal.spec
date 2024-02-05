ghost mathint total_sent {
    init_state axiom total_sent == 0;
} 

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    total_sent = total_sent + value;
}

invariant inv()
    total_sent <= to_mathint(currentContract._deposited);
