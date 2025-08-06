rule ab_eq_ac {
    env e;
    assert currentContract.getAB(e) == currentContract.getAC(e);
}