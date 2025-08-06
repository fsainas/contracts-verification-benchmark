function invariant() public view {
    assert(getAB() % 3 == 0);
}