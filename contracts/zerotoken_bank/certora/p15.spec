rule P15 {
    env e;

    deposit(e, 0);
    withdraw@withrevert(e, balanceOf(e.msg.sender));

    assert(!lastReverted);
    assert(balanceOf(e.msg.sender) == 0);
}
