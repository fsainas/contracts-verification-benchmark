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

        balance -= _amount;
        sent += _amount;
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.55s
// Targets: "all"
// ----
