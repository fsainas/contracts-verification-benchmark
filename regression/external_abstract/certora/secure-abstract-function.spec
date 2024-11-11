methods {
	function D.d() external => HAVOC_ALL;
}
rule secure_abstract_function {
	env e;
	uint256 x_before = currentContract.x;
	g(e);
	assert(currentContract.x == x_before);
}