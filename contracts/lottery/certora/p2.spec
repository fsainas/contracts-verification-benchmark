rule P2 {
    env e;
    method f;
    calldataarg args;

    address prev_last_player = getLastPlayer();
    f(e, args); 
    address last_player = getLastPlayer();
    
    assert (
        prev_last_player != e.msg.sender && 
        last_player == e.msg.sender
        ) => f.selector == sig:enter().selector;
}

// certoraRun Lottery_v1.sol:Lottery --verify Lottery:Lottery_p2.spec --optimistic_loop
