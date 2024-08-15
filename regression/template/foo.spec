methods {
	function f() external;
}

rule foo {

    env e;

    mathint x = f(e);

    assert x == 0;

}