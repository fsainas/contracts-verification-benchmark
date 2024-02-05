rule reclaim_not_revert {
    env e;
    
    require(getBalance() < getGoal());
    require(e.block.number > getEndDonate());
    require(getDonated(e.msg.sender) > 0);
    require(e.msg.value == 0);
    
    reclaim@withrevert(e);    

    assert !lastReverted;
}

