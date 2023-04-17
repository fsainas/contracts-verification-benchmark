// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    uint sent;
    uint deposited;

    constructor () payable {
        deposited = address(this).balance;
    }

    function withdraw(uint _amount) public {
        require(_amount <= address(this).balance);
        sent += _amount;
        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.53s
// Targets: "assert"
// ----
// Warning: CHC: Assertion violation happens here - line 21
// ----
