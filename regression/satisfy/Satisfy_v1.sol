// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.25;
contract Satisfy {
    uint r0;
    uint r1;
    function f(uint a, uint b) public view{
        require(b == r1 * a / r0 && b * r0 == r1 * a, "Error: r1 * a / r0 != b");
    }
}