// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {
    
    constructor () payable {
    }

    function withdraw(uint amount) public nonReentrant {
        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant(uint amount) public {
	uint _prev_balance = address(this).balance;	
	withdraw(amount);
        assert(address(this).balance <= _prev_balance);
    }
}
