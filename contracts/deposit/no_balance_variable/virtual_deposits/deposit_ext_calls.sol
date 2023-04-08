// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Deposit {

    uint sent;

    uint deposited;

    constructor () {
        deposited = address(this).balance;
    }

    function deposit(uint _amount) public {
        deposited += _amount;
    }

    function withdraw(uint _amount) public {
        require(_amount <= address(this).balance);
        sent += _amount;
        
        (bool succ, ) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function withdraw_all() public {
        sent += address(this).balance;

        (bool succ, ) = msg.sender.call{value: address(this).balance}("");
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 4:27.45s
// Targets: "all"
// ----
// Does not seem to terminate
// Warning: CHC: Overflow line 15
// Warning: CHC: Overflow line 20
// Warning: CHC: Overflow line 27
// Warning: CHC: Assertion violation happens here line 34
// ----
