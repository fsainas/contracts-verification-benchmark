rule correct_modulo_ab {
    env e;
    assert currentContract.getAB(e) % 3 == 0;
}