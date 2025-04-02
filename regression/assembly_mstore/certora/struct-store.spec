rule struct_store {
    env e;
    f(e);
    assert(currentContract.s.x == 7);
}