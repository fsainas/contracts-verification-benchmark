rule withdraw_revert {
    env e;
    address receiver;
    uint amount;

    withdraw@withrevert(e, receiver, amount);

    assert(!lastReverted => e.msg.sender == currentContract.owner);
}
rule finalize_revert {
    env e;

    finalize@withrevert(e);

    assert(!lastReverted => e.msg.sender == currentContract.owner);
}
