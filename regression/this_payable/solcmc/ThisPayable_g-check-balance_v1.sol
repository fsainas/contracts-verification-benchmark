contract ThisPayable {
	function g(uint i) public {
		require(address(this).balance == 100);
		this.h{value: i}();
		assert(address(this).balance == 100);
	}
	function h() external payable {}
}