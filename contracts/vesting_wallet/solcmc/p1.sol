// p1: the amount of releasable tokens is always <= the contract balance

function invariant() public view {
    assert(releasable() <= address(this).balance);
}
