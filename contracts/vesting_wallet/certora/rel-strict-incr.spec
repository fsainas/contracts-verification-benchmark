rule P8 {
    mathint start = getStart();
    mathint duration = getDuration();
    
    env e1;
    
    mathint releasable1 = releasable(e1);
    mathint balance1 = getBalance();
    mathint timestamp1 = e1.block.timestamp;
    mathint released1 = currentContract.released;
    
    env e2;

    mathint releasable2 = releasable(e2);
    mathint balance2 = getBalance();
    mathint timestamp2 = e2.block.timestamp;
    mathint released2 = currentContract.released;


    require balance1 == balance2 && released2 == released1;
    require start+duration > timestamp2 && timestamp2 > timestamp1 && timestamp1 > start;
    
    assert releasable2 > releasable1;
}
