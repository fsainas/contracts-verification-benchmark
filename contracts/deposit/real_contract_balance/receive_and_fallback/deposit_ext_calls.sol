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
// Time: 4:12.55
// Targets: "all"
// ----
// Does not seem to terminate
// ----
