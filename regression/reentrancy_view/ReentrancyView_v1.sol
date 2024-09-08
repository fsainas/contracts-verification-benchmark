//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_reentrancy_view.sol
pragma solidity ^0.8.25;

contract ReentrancyView {
	uint x;
	function s(uint _x) public view {
		x == _x;
	}
	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
	}
	function getX() public view returns (uint) {
		return x;
	}
}