//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_return_1.sol
pragma solidity ^0.8.25;

contract CallVerifier {
	uint x;
	bool callSuccessful;
	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
		callSuccessful = s;
	}
}