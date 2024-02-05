function invariant(address addr) public {
    assert(balances[addr] >= 0);
}
