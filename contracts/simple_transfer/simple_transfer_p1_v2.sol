// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint sent;
    uint deposited;
    uint balance;

    constructor () payable {
        balance = address(this).balance;
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
// Time: 0.70s
// Targets: "assert"
// ----
