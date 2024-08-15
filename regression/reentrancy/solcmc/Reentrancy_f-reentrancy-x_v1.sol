contract Reentrancy {
	uint x;
	function s(uint _x) public {
		x = _x;
	}
	function f(address a) public {
		require(x == 0);
		(bool s, bytes memory data) = a.call("");
		assert(x == 0);
	}
}