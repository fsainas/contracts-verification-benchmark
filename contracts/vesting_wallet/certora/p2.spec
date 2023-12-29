rule P2 {
    env e;
    mathint ending_timestamp = getStart() + getDuration();
    mathint current_timestamp = e.block.timestamp;
    require current_timestamp > ending_timestamp;
    assert releasable(e) >= getBalance();
}