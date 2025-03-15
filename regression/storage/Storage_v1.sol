// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.25;

contract Storage {
    uint x;
    function f(uint n) public {
        x = x + n;
    }
    function sum(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
}