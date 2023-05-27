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
        require(amount > 0);
        require(amount <= balance);

        balance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
