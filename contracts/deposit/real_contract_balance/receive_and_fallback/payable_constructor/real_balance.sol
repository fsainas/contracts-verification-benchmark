// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint sent;

    uint deposited;

    constructor () payable {
        deposited = address(this).balance + msg.value;  // real balance + ether received
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
        assert(sent <= deposited);      // should fail
    }
}
// ====
// SMTEngine: CHC
// Time: 3.88s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 11
// Warning: CHC: Overflow line 15
// Warning: CHC: Overflow line 19
// Warning: CHC: Overflow line 26
// Warning: CHC: Overflow line 34
// Warning: CHC: Assertion violation happens here
// ----
