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

    receive() external payable {
        balance += msg.value;
        deposited += msg.value;
    }

    fallback() external payable {
        balance += msg.value;
        deposited += msg.value;
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function withdraw_all() public {

        sent += balance;
        balance = 0;

        (bool succ,) = msg.sender.call{value: address(this).balance}("");       // real balance
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 31.29s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 18
// Warning: CHC: Overflow line 22
// Warning: CHC: Overflow line 23
// ----
