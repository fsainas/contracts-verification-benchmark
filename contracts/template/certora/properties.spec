methods {
    function f(address) external;
    function getBalance() external returns (uint) envfree;
    function getX() external returns (uint) envfree;
}

rule P1 {
    assert getX() == getX();
}
