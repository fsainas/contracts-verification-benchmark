// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {

    constructor () payable {
    }

    // v4
    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance - 1);

	(bool succ,) = msg.sender.call{value: amount-1}("");
        require(succ);
    }
}
