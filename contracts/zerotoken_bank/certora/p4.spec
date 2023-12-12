rule P4 {
    env e;
    uint amount;

    require(amount <= balanceOf(e.msg.sender));

    withdraw@withrevert(e, amount);

    assert(!lastReverted);
}
