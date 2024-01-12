rule P2 {
    env e;

    mathint current_timestamp = e.block.timestamp;
    mathint ending_timestamp = getStart() + getDuration();
    
    require current_timestamp > ending_timestamp;

    assert releasable(e) == getBalance();
}
