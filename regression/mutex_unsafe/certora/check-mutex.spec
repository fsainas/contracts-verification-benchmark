methods {
    function getX() external returns (uint) envfree;
}

rule check_mutex {
	env e; 
	address a;
	mathint x_before = getX();
	f(e, a);
	mathint x_after = getX();
	assert(x_before == x_after);
}