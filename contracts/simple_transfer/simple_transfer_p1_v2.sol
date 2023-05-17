// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    // ghost variables
    uint _sent;
    uint _deposited;
    uint _balance;

    constructor () payable {
        _balance = address(this).balance;
        _deposited = _balance;
    }

    function withdraw(uint amount) public {
        require(amount <= _balance);
        _sent += amount;
        _balance -= amount;
        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant() public view {
        assert(_sent <= _deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.70s
// Targets: "assert"
// ----
