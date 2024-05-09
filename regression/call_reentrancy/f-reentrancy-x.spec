rule f_reentrancy_x {
	env e; 
	address a;
	f(e, a);
	assert(currentContract.x == 0);
}