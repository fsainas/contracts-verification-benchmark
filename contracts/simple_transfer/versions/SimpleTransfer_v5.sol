// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version `withdraw` requires a balance of at least `amount+1` instead of `amount`.
contract SimpleTransfer is ReentrancyGuard {

    uint private sent;
    uint public immutable initial_deposit;

    constructor () payable {
        initial_deposit = address(this).balance;
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance + 1);

        sent += amount;

	    (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}
