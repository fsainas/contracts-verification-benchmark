rule withdraw_not_revert {
    env e;
    uint amount;

    require(amount <= getBalance(e.msg.sender));

    withdraw@withrevert(e, amount);

    assert(!lastReverted);
}