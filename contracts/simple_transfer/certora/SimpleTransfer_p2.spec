methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
}

rule P2 {
    env e;
    uint amount;

    mathint before = getBalance();
    withdraw(e, amount);
    mathint after = getBalance();

    assert before >= after;
}