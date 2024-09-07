contract CallRevert {
	uint x;
	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
		assert(s);
	}
}
