//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/special/gasleft.sol
pragma solidity ^0.8.25;

contract GasLeft {
	function f() public {
		uint g = gasleft();
        uint after_assignment = gasleft();
	}
}