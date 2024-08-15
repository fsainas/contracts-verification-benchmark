contract Payable {
	function g(address payable i) public {
		require(address(this).balance == 100);
		i.call{value: 10}("");
		assert(address(this).balance == 90);
	}
}