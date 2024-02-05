rule donate_not_revert_overflow {
    env e;
    
    require(e.block.number <= getEndDonate());
    require(e.msg.value <= balanceOf(e.msg.sender));
    mathint n = getDonated(e.msg.sender);

    require(n < max_uint - e.msg.value);

    donate@withrevert(e);

    assert !lastReverted;
}
