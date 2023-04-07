// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Simple {

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

        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function withdraw_all() public {

        uint amount = balance;

        sent += balance;
        balance = 0;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 11:13.28s
// Targets: "all"
// ----
// Does not seem to terminate.
// ====
// SMTEngine: CHC
// Time: 2.00s
// Targets: "assert"
// ----
