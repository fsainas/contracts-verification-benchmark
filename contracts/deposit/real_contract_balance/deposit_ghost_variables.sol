// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint balance;
    uint sent;

    uint deposited;

    constructor () {
        balance = address(this).balance;    // real balance
        deposited = balance;
    }

    function deposit(uint _amount) public {
        balance += _amount;
        deposited += _amount;
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;
    }

    function withdraw_all() public {

        sent += balance;
        balance = 0;
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 14.00s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 17
// Warning: CHC: Overflow line 18
// ----
