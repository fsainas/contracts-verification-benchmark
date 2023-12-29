rule P3 {
    env e;

    mathint start = currentContract.start;
    mathint current_timestamp = e.block.timestamp;
    
    require current_timestamp < start;
    assert releasable(e) <= 0;
}