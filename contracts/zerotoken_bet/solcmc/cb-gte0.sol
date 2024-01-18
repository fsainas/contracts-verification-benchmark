// the contract balance is non-negative

function invariant() public view {
    assert (balance >= 0);
}
