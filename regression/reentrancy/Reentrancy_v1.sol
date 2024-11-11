//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_reentrancy_1.sol
pragma solidity ^0.8.25;

contract Reentrancy {
	uint x;
	function s(uint _x) public {
		x = _x;
	}
	function f(address a) public {
		require(x == 0);
		(bool s, bytes memory data) = a.call("");
	}
}