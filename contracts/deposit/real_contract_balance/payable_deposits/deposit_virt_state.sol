// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint balance;
    uint sent;

    uint deposited;

    constructor () {
        balance = address(this).balance;
        deposited = address(this).balance;
    }

    function deposit() public payable {
        balance += msg.value;
        deposited += msg.value;
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
// Time: 15.89s
// Targets: "all"
// ----
