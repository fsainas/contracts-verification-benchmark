// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint balance;
    uint sent;

    uint deposited;

    constructor () payable {
        balance = address(this).balance + msg.value;    // real balance + ethers received
        deposited = balance;
    }

    function deposit() public payable {
        balance += msg.value;           // ethers received
        deposited += msg.value;         // ethers received
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        uint succ = block.number % 2;

        if (succ == 0) {
            sent -= _amount;
            balance += _amount;
        }
    }

    function withdraw_all() public {

        uint amount = balance;

        sent += balance;
        balance = 0;

        uint succ = block.number % 2;

        if (succ == 0) {
            sent -= amount;
            balance += amount;
        }

    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 6.09s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 12
// Warning: CHC: Overflow line 17
// Warning: CHC: Overflow line 18
// ----
