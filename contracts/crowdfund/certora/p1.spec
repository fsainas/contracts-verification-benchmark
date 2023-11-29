rule P1 {
    env e;
    
    uint balance = getBalance();
    uint goal = getGoal();
    require balance < goal;
    
    withdraw@withrevert(e);    

    assert lastReverted;
}

