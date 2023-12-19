function invariant() public view {
    assert(owner != recovery);
}
