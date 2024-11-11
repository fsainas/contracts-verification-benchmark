pragma solidity ^0.8.25;

contract CallVerifier {
	uint x;
	bool callSuccessful;

	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
		callSuccessful = s;
	}

	function getCallSuccessful() public view returns(bool){
		return callSuccessful;
	}
}