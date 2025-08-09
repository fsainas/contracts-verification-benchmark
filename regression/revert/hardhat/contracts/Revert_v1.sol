//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/control_flow/revert_complex_flow.sol
pragma solidity ^0.8.25;

contract Revert {
    uint c;
    uint x;
	function f(bool b, uint a) public {
		require(a <= 256);
        x = a;
		if (b)
			revert();
		c = a + 1;
		if (b)
			c--;
		else
			c++;
	}

	function get_c () public view returns (uint) {
		return c;
	}
}