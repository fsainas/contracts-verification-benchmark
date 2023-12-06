// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version reentrant `withdraw`.
contract SimpleTransfer {

    // ghost variables p1
    uint _sent;
    uint _deposited;

    constructor () payable {
        // p1
        _deposited = address(this).balance;
    }

    function withdraw(uint amount) public {
        require(amount <= address(this).balance);

        // p1
        _sent += amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);	
    }

}
