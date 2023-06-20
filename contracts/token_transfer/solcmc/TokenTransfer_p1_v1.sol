// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/ERC20v1.sol";

contract TokenTransfer {
        
    ERC20 token;
    bool ever_deposited;

    // ghost variables
    uint _sent;
    uint _deposited;
    
    // v1
    constructor(ERC20 token_) {
        token = token_;
    }

    // v1
    function deposit() external {
	// require (msg.sender != address(0));
        require (!ever_deposited);
	
        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.transferFrom(msg.sender, address(this), allowance);

        _deposited = allowance;
    }

    // v1
    function withdraw(uint amount) external {
        require (ever_deposited);	
	require (msg.sender != address(0));	
        require (amount <= token.balanceOf(address(this)));
	
        token.transfer(msg.sender, amount);

        _sent += amount;	
    }

    // p1
    function invariant() public view {
        assert(_sent <= _deposited);
	// assert(_deposited == 0);
	// assert(_sent >= 0);	
	// assert(token.totalSupply() == 0);
    }
}

