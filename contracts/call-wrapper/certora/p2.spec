rule P2 {
    env e;
    address called;

    mathint before = getData();
    callwrap(e, called);
    mathint after = getData();

    assert before == after;
}
