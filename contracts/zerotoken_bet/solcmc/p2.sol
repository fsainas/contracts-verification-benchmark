
// the contract balance does not exceed 2 tokens

function invariant() public view {
    assert (balance <= 2);
}
