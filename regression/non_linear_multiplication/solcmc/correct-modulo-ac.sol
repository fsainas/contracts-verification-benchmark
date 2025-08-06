function invariant() public view {
    assert(getAC() % 3 == 0);
}