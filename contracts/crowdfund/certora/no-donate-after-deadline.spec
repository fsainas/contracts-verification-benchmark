rule no_donate_after_deadline {
    env e;
        
    require(e.block.number > getEndDonate());

    donate@withrevert(e);    
    assert lastReverted;
}


