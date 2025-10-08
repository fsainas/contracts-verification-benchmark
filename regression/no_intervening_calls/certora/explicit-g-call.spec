methods {
    function f() external envfree;
    function g() external;
}
rule explicit_g_call {
    env e;
	require(currentContract.b);
    f();
    g(e);
    f(); 
    assert (currentContract.b);
}