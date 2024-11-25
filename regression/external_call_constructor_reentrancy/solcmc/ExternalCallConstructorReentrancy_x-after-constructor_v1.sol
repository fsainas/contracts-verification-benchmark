//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/external_call_from_constructor_1.sol
pragma solidity ^0.8.25;

interface D {
	function ext(ExternalCallConstructorReentrancy c) external returns (uint);
}

contract ExternalCallConstructorReentrancy {
	uint x;
	function s(uint _x) public { x = _x; }
	constructor(D d) {
		require(x == 0);
		uint a = d.ext(this);
		assert(x == 0);
	}
}