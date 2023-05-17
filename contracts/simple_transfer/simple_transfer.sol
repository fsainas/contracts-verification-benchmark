// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    constructor () payable { }

    function withdraw(uint _amount) public {
        (bool succ,) = msg.sender.call{value: _amount}("");
        require(succ);
    }

}
