function invariant() public view {
    assert (!ever_deposited || supply > 0);
}
