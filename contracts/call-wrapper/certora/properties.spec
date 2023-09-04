methods {
    function callwrap(address) external;
    function getBalance() external returns (uint) envfree;
    function getData() external returns (uint) envfree;
}

rule P1 {
    env e;
    address called;

    mathint before = getBalance();
    callwrap(e, called);
    mathint after = getBalance();

    assert before == after;
}

rule P2 {
    env e;
    address called;

    mathint before = getData();
    callwrap(e, called);
    mathint after = getData();

    assert before == after;
}
