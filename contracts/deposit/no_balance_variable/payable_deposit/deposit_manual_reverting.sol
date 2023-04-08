// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint sent;

    uint deposited;

    constructor () {
        deposited = address(this).balance;
    }

    function deposit() public payable {
        deposited += msg.value;
    }

    function withdraw(uint _amount) public {
        require(_amount <= address(this).balance);
        sent += _amount;

        uint succ = block.number % 2;

        if (succ == 0) sent -= _amount;
    }

    function withdraw_all() public {
        sent += address(this).balance;

        uint succ = block.number % 2;

        if (succ == 0) sent -= address(this).balance;
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 2.42s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 20
// Warning: CHC: Overflow line 28
// Warning: CHC: Assertion violation happens here line 36
// ----
