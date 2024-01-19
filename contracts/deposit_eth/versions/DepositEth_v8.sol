// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version `withdraw` callable only by EOAs.
contract DepositEth {

    uint private sent;
    uint public immutable initial_deposit;

    address private immutable owner;

    constructor () payable {
        initial_deposit = address(this).balance;
        owner = msg.sender;
    }

    function withdraw(uint amount) public {
        // check EOA
        require(msg.sender == tx.origin);

        require(amount <= address(this).balance);

        sent += amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}
