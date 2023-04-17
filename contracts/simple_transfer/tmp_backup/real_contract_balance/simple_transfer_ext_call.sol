// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint balance;
    uint sent;

    uint deposited;

    constructor () payable {
        balance = address(this).balance + msg.value;
        deposited = balance;
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 2.00s
// Targets: "all"
// ----
// Warning: CHC: Overflow line 12
// ----
