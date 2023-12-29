rule P3 {
    env e;
    mathint start = getStart();
    mathint current_timestamp = e.block.timestamp;
    assert current_timestamp < start => releasable(e) <= 0;
}