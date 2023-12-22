// p3: if the vesting scheme has not started yet, then no balance is releasable

function invariant() public view {
    // block.timestamp < start => releasable() == 0
    assert(!(block.timestamp < start) || releasable() == 0);
}