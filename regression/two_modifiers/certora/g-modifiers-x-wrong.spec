rule f_modifiers_x_wrong {
    env e;
    g(e);
    assert(currentContract.x == 3);
}