// p2: if the vesting scheme has expired, that the whole contract balance is releasable

function invariant() public view {
    // block.timestamp > start + duration => releasable() >= address(this).balance
    require(block.timestamp > start + duration);
    assert(releasable() == address(this).balance);
}