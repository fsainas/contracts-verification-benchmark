//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

/// @custom:version conformant to specification
contract Bank {
    uint initial;

    constructor() {
        initial = address(this).balance;
    }

    function balanceOf(address a) public view returns (uint) {
        return a.balance;
    }
}
