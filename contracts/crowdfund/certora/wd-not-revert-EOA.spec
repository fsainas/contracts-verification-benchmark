rule wd_not_revert_EOA {
    env e;
    
    require(getBalance() >= getGoal());
    require(e.block.number > getEndDonate());
    require(e.msg.value == 0);
    
    require(e.msg.sender==e.tx.origin);
    
    withdraw@withrevert(e);    

    assert !lastReverted;
}

