// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version reentrant `withdraw`.
contract SimpleTransfer {

    uint private sent;
    uint public immutable initial_deposit;

    constructor () payable {
        initial_deposit = address(this).balance;
    }

    function withdraw(uint amount) public {
        require(amount <= address(this).balance);

        sent += amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);	
    }

}
