methods {
    function balanceOf(address) external returns(uint) envfree;
}
rule g_check_balance {
	env e; 
	uint i;
	g(e, i);
	assert(balanceOf(currentContract) == 100);
}