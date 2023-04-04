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

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        uint success = block.number % 2;

        if (success == 0) {
            sent -= _amount;
            balance += _amount;
        }
    }

    function invariant() public view {
        assert(sent <= init_balance);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.99s
// Targets: "all"
// ----
