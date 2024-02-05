rule any_user_can_picker {
    env e;
    
    require e.msg.value == 0;
    require to_mathint(e.block.number) > currentContract.start + currentContract.duration;
    pickWinner@withrevert(e);
    
    assert !lastReverted;
    assert currentContract._picked;
}
