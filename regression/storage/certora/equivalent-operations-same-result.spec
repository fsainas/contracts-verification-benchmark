using Storage as s;

methods {
    function f(uint n) external envfree;
    function sum(uint a, uint b) external returns (uint) envfree;
}
rule equivalent_operations_same_result {
    uint a;
    uint b;
    uint total;
    uint sum = currentContract.sum(a, b);
    require(a + b <= max_uint256);

    storage initial = lastStorage;
    f(a) at initial;
    f(b);
    storage afterF = lastStorage;

    f(sum) at initial;
    storage afterSecondF = lastStorage;

    assert(afterF == afterSecondF);
}