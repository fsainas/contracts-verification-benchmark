methods {
    function balanceOf(address) external returns(uint) envfree;
}
rule g_check_balance {
	env e; 
	calldataarg args;
	g(e, args);
	assert(balanceOf(currentContract) == 90);
}