pragma solidity ^0.8.25;

contract Revert {
    function f(bool b, uint a) pure public {
		require(a <= 256);
		if (b)
			revert();
		uint c = a + 1;
		if (b)
			c--;
		else
			c++;
		assert(c == a);
	}
}