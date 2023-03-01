contract C
{
	function f(uint x) public pure {
		do {
			x = x + 1;
		} while (x < 1000);
		assert(x > 0);
	}
}
