methods {
    function getX() external returns (uint) envfree;
}

rule f_reentrancy_view_x {
	env e; 
	address a;
	mathint x_before = currentContract.x;
	f(e, a);
	mathint x_after = currentContract.x;
	assert(x_before == x_after);
}