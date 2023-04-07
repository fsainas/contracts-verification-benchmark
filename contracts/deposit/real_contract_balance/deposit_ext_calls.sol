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
// Time: 14.39s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 17
// Warning: CHC: Overflow line 18
