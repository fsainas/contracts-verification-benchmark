rule any_user_can_enter {
    env e;
    require e.msg.value == 10^16;
    require e.msg.value <= balanceOf(e.msg.sender);
    require currentContract.start <= e.block.number;
    require to_mathint(e.block.number) <= currentContract.start + currentContract.duration;

    enter@withrevert(e);
    
    assert !lastReverted;
}
