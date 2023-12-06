// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version non-reentrant `withdraw`, using [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol).
contract SimpleTransfer is ReentrancyGuard {

    // ghost variables p1
    uint _sent;
    uint _deposited;

    constructor () payable {
        // p1
        _deposited = address(this).balance;
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance);

        // p1
        _sent += amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}
