rule no_wd_if_no_goal {
    env e;
    
    uint balance = getBalance();
    uint goal = getGoal();
    require balance < goal;
    
    withdraw@withrevert(e);    

    assert lastReverted;
}

