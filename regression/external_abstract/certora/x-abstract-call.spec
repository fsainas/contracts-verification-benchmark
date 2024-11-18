methods {
	function _.d() external => HAVOC_ALL;
}
rule x_abstract_call {
	env e;
	uint256 x_before = currentContract.x;
	g(e);
	assert(currentContract.x == x_before);
}