contract ReentrancyView {
	uint x;
	function s(uint _x) public view {
		x == _x;
	}
	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
		assert(x == 0);
	}
}