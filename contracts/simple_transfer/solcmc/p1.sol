function invariant() public view {
    assert(_sent <= _deposited);
}
