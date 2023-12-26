rule P4 {
    env e1;
    
    mathint releasable1 = releasable(e1);
    mathint balance1 = getBalance();
    mathint timestamp1 = e1.block.timestamp;

    env e2;

    mathint releasable2 = releasable(e2);
    mathint balance2 = getBalance();
    mathint timestamp2 = e2.block.timestamp;
    
    mathint start = getStart();

    require timestamp1 > start && timestamp2 > start;

    assert (
        timestamp2 > timestamp1 && 
        balance1 == balance2
        ) => releasable2 > releasable1;
}