//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract Bank is ReentrancyGuard {

    mapping (address => uint256) accounts;

    receive() external payable nonReentrant {
        accounts[msg.sender] += msg.value;
        assert(address(this).balance >= msg.value);
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount > 0);
        require(amount <= accounts[msg.sender]);

        accounts[msg.sender] -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: n/a
// ----
