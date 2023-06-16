// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {

    // ghost variables
    uint _sent;
    uint _deposited;
    
    constructor () payable {
        _deposited = address(this).balance;	
    }

    // v5
    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance + 1);

        _sent += amount;
	
	(bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }
    
    // p1
    function invariant() public view {
        assert(_sent <= _deposited);
    }
}
