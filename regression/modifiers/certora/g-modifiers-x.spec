rule f_modifiers_x {
    env e;
    g(e);
    assert(currentContract.x == 7);
}