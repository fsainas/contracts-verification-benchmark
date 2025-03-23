methods {
    function f(uint a, uint b) external envfree;
}
rule f_call_not_revert {
    uint a;
    uint b;

    f@withrevert(a, b);
    satisfy(!lastReverted);
}