rule P3 {
    env e;
    uint amount;

    deposit@withrevert(e, amount);

    assert(!lastReverted);
}
