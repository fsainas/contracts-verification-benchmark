rule no_wd_if_no_goal {
    env e;
    
    require getBalance() < getGoal();
    
    withdraw@withrevert(e);    
    assert lastReverted;
}

