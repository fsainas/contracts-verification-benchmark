//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    uint private balance;
    address private owner;

    // ghost variables
    uint _prev_balance;

    constructor(address owner_) {
        owner = owner_;
    }

    receive() external payable {
        balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner);
        require(amount > 0);
        require(amount <= balance);

        balance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

    function invariant(uint amount) public {
        _prev_balance = balance;
        withdraw(amount);
        assert(_prev_balance > balance);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: 0.99s
// ----
// Warning: CHC: Assertion violation happens here - line 34
