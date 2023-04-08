// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint sent;

    uint deposited;

    constructor () {
        deposited = address(this).balance;
    }

    receive() external payable {
        deposited += msg.value;
    }

    fallback() external payable {
        deposited += msg.value;
    }

    function withdraw(uint _amount) public {
        require(_amount <= address(this).balance);
        sent += _amount;
    }

    function withdraw_all() public {
        sent += address(this).balance;
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 27.77s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 24
// Warning: CHC: Overflow line 28
// Warning: CHC: Assertion violation happens here line 32
// ----
