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

    function foo(uint amount) public pure returns (uint) {
        // require(amount >= 0);
	return 100;
    }    

    // p2
    function invariant(uint amount) public {
	require(amount <= address(this).balance && amount >= 0);
        (bool success, ) = address(this).call(abi.encodeWithSignature("foo(uint)", 1));
	// verification always fails
	// assert(success);
    }
}

contract Test {
    SimpleTransfer private _c;

    constructor(SimpleTransfer c) {
        _c = c;
    }

    function invariant(uint amount) public {
        try _c.foo(amount) returns (uint result) {
	    assert(result == 100);
        } catch {
	    // verification always fails	    
            assert(false);
        }
    }
}
