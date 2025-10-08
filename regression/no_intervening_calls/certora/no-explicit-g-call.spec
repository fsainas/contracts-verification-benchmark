methods {
    function f() external envfree;
}
rule no_explicit_g_call {
	require(currentContract.b);
    f();
    f(); 
    assert (currentContract.b);
}