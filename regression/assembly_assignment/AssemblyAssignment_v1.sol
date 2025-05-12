//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/inline_assembly/local_var.sol
pragma solidity ^0.8.29;

contract AssemblyAssignment{
	function f(uint x) public pure returns (uint) {
		assembly {
			x := 2
		}
		return x;
	}
}