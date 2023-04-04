// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint balance;
    uint sent;

    uint init_balance;

    constructor (uint _deposit) {
        require(_deposit > 0);
        balance = _deposit;
        init_balance = balance;
    }

    function withdraw(uint _amount) public {

        require(_amount <= balance);

        sent += _amount;
        balance -= _amount;

        (bool succ,) = msg.sender.call{value: sent}("");
        require(succ);
    }

    function invariant() public view {
        assert(sent <= init_balance);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.55s
// Targets: "all"
// ----
