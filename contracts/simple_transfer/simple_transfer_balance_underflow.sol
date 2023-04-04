// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint balance;
    uint sent;

    uint init_balance;

    constructor (uint _deposit) {
        balance = _deposit;
        init_balance = balance;
    }

    function withdraw(uint _amount) public {
        balance -= _amount;
        sent += _amount;
    }

    function invariant() public view {
        assert(sent <= init_balance);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.13s
// Targets: "assert"
// ----
// SMTEngine: CHC
// Time: 0.67s
// Targets: "all"
// Warning: CHC: Underflow line 17
// ----
