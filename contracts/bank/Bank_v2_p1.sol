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
        assert(address(this).balance >= balance);
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner);
        require(amount > 0);
        require(amount <= balance);

        balance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: 0.47s
// ----
