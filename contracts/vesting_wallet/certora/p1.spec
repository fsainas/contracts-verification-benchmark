rule P1 {
    env e;
    assert releasable(e) <= getBalance();
}
