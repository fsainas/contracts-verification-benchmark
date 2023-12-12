rule P9 {
    env e;

    uint amount = assert_uint256(max_uint256 - balanceOf(e.msg.sender));
    deposit@withrevert(e, amount);

    assert(!lastReverted);
    assert(balanceOf(e.msg.sender) == max_uint256);
}
