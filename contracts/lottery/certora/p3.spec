rule P3 {
    env e;

    address prev_last_player = getLastPlayer();
    enter(e); 
    address last_player = getLastPlayer();
    
    assert (
        prev_last_player != e.msg.sender && 
        last_player == e.msg.sender
        ) => f.selector == sig:enter().selector;
}

// certoraRun Lottery_v1.sol:Lottery --verify Lottery:Lottery_p2.spec --optimistic_loop
