//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/external_call_from_constructor_1.sol
pragma solidity ^0.8.25;

contract State {
	function f(uint _x) public pure returns (uint) {
		require(_x < 100);
		return _x;
	}
}
contract ExternalCallConstructor {
	State s;
	uint z = s.f(2);

	function f() public view{}
}