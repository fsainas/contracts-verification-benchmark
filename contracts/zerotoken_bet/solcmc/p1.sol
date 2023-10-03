
// the contract balance is always nonnegative

function invariant() public view {
    assert (balance >= 0);
}
