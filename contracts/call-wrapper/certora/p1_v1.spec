rule P1 {
    env e;
    address called;

    mathint before = getBalance();
    callwrap(e, called);
    mathint after = getBalance();

    assert false;
}
