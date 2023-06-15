// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {
    
    constructor () payable {
    }

    // v3
    function withdraw(uint amount) public nonReentrant {
        (bool succ,) = address(0).call{value: amount}("");
        require(succ);
    }

    // p3
    function invariant(uint amount) public {
	uint _prev_sender_balance = address(msg.sender).balance;
	withdraw(amount);
	uint _sender_balance = address(msg.sender).balance;	
        assert(_sender_balance == _prev_sender_balance + amount);
    }
}
