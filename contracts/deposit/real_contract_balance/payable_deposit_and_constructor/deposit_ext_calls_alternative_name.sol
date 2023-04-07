// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Simple {

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
// Time: 24.17s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 12
// Warning: CHC: Overflow line 17
// Warning: CHC: Overflow line 18
