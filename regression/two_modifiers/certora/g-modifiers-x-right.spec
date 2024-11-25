rule f_modifiers_x_right {
    env e;
    g(e);
    assert(currentContract.x == 7);
}