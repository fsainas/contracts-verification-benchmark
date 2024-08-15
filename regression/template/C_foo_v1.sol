// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

// Instrument this contract for Solcmc
contract C {

	uint x = 0;

	function f() view public returns (uint) {
		assert(x == 0);

		return x;
	}

}
