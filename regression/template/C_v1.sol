// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

contract C {

	uint x = 0;

	function f() view public returns (uint) {
		return x;
	}

}
