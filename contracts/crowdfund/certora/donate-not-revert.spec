rule donate_not_revert {
    env e;
    
    require(e.block.number <= getEndDonate());
    require(e.msg.value <= balanceOf(e.msg.sender));

    donate@withrevert(e);    

    assert !lastReverted;
}

