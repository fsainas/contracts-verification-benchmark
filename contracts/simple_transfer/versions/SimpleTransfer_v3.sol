// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version `withdraw` transfers to `address(0)` instead of `msg.sender`.
contract SimpleTransfer is ReentrancyGuard {

    uint private sent;
    uint public immutable initial_deposit;

    constructor () payable {
        initial_deposit = address(this).balance;
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance);

        sent += amount;

	    (bool succ,) = address(0).call{value: amount}("");
        require(succ);
    }

}
