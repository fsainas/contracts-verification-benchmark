// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint sent;

    uint deposited;

    constructor () {
        deposited = address(this).balance;      // real balance
    }

    receive() external payable {
        deposited += msg.value;
    }

    fallback() external payable {
        deposited += msg.value;
    }

    function withdraw(uint _amount) public {

        require(_amount <= address(this).balance);      // real balance

        sent += _amount;

        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function withdraw_all() public {

        sent += address(this).balance;      // real balance

        (bool succ,) = msg.sender.call{value: address(this).balance}("");   // real balance
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 6:24.62s
// Targets: "all"
// ----
// Does not seem to terminate
