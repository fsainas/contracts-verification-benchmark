rule correct_modulo_ac {
    env e;
    assert currentContract.getAC(e) % 3 == 0;
}