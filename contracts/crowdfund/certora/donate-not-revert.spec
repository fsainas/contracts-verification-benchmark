rule donate_not_revert {
    env e;
    
    require(e.block.number <= getEndDonate());

    donate@withrevert(e);    

    assert !lastReverted;
}

