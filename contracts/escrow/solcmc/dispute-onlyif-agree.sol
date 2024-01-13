function invariant() public {
    Escrow.State prev_state = state;
    open_dispute();
    assert(prev_state==State.AGREE);

}