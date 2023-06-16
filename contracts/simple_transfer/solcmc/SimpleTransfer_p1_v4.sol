// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    // ghost variables
    uint _sent;
    uint _deposited;

    constructor () payable {
        _deposited = address(this).balance;
    }

    // v4
    function withdraw(uint amount) public {
        require(amount <= address(this).balance - 1);

        _sent += amount-1;
	
	(bool succ,) = msg.sender.call{value: amount-1}("");
        require(succ);
    }
    
    // p1
    function invariant() public view {
        assert(_sent <= _deposited);
    }
}
