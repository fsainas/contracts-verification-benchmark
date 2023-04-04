// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint balance;
    uint sent;

    uint deposited;

    constructor (uint _deposit) {
        balance = _deposit;
        deposited = balance;
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function deposit() public payable {
        balance += msg.value;
        deposited += msg.value;
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 4.20s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 28
// Warning: CHC: Overflow line 29
