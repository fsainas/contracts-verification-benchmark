// the supply is more than zero if a deposit has been made

function invariant() public view {
    assert (!ever_deposited || supply > 0);
}
