//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract Bank is ReentrancyGuard {

    uint private balance;
    address private owner;

    constructor(address owner_) {
        owner = owner_;
    }

    receive() external payable nonReentrant { 
        balance += msg.value;
    }

    function withdraw(uint amount) public nonReentrant {
        require(msg.sender == owner);
        require(amount <= balance);

        balance -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
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
// Time: 1.86s
// ----
