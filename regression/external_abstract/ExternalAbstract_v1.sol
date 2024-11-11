//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/external.sol
pragma solidity ^0.8.25;

abstract contract D {
	function d() external virtual;
}

contract ExternalAbstract {
	uint x;
	D d;
	function f() public {
		if (x < 10)
			++x;
	}
	function g() public {
		require(x < 10);
		d.d();
	}
	function getX() public view returns (uint) {
		return x;
	}
}