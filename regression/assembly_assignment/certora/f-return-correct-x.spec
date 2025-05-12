rule f_return_correct_x {
    env e;
    uint x;
    assert(f(e, x) == 2);
}