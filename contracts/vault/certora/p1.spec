rule P1 {
    env e;
    bool b;

    if (b) {
        address receiver;
        uint amount;
        withdraw@withrevert(e, receiver, amount);
    } else {
        finalize@withrevert(e);
    }
    assert(!lastReverted => e.msg.sender == getOwner());
}
