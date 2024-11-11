pragma solidity ^0.8.25;

contract GasLeft {
	uint g;
	uint after_assignment;
	function f() public {
		g = gasleft();
		after_assignment = gasleft();
	}
	function getG() public view returns (uint) {
		return g;
	}
	function getAfterAssignment() public view returns (uint) {
		return after_assignment;
	}
}