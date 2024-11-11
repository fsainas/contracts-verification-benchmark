pragma solidity ^0.8.25;

contract GasLeft {
    function f() public view {
		uint g = gasleft();
		assert(g >= gasleft());
	}
}