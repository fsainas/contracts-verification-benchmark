rule P1_withdraw {
    env e;
    address receiver;
    uint amount;

    withdraw@withrevert(e, receiver, amount);

    assert(!lastReverted => e.msg.sender == currentContract.owner);
}
rule P1_finalize {
    env e;

    finalize@withrevert(e);

    assert(!lastReverted => e.msg.sender == currentContract.owner);
}
