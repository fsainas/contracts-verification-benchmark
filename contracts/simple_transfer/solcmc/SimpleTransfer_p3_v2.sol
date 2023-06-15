// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {
    
    constructor () payable {
    }

    // v2
    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance);		
        (bool succ,) = msg.sender.call{value: amount}("");
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
