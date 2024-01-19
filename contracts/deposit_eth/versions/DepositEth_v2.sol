// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol"; // https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol

/// @custom:version non-reentrant `withdraw`.
contract DepositEth is ReentrancyGuard {

    uint private sent;
    uint public immutable initial_deposit;

    constructor () payable {
        initial_deposit = address(this).balance;
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance);

        sent += amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}
