//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    uint private balance;
    address private owner;

    constructor(address owner_) {
        owner = owner_;
    }

    receive() external payable { 
        balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner);
        require(amount <= balance);

        balance -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);

        assert(msg.sender == owner);
    }

    function invariant(uint amount) public {
        require(amount > 0);
        require(amount <= balance);
        uint prev_balance = balance;
        withdraw(amount);
        assert(prev_balance > balance);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: 1.54s
// ----
// Warning: CHC: Assertion violation happens here - line 34
