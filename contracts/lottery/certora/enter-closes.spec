rule enter_closes {
    env e;
    
    require to_mathint(e.block.number) > currentContract.start + currentContract.duration;
    enter@withrevert(e);
    
    assert lastReverted;
}
