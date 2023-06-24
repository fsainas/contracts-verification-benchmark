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

    // p4: a transaction `withdraw(amount)` is not reverted whenever `amount` does not exceed the contract balance
    function invariant(uint amount) public {
	require(amount <= address(this).balance && amount >= 0);

	// ensures that the sender is a EOA
	require(msg.sender == tx.origin);	
        try this.withdraw(amount)  {
        } catch {
	    // verification always fails	    
            assert(false);
        }
	
	// alternative encoding of p4 (verification always fails)
        // (bool success, ) = address(this).call(abi.encodeWithSignature("withdraw(uint)", 1));
	// assert(success);
    }
}

