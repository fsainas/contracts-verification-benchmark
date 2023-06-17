// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";

contract TokenTransfer {

    IERC20 token;
    bool ever_deposited;

    // ghost variables
    uint _sent;
    uint _deposited;
    
    // v1
    constructor(IERC20 token_) {
        token = token_;
    }

    // v1
    function deposit() external {
        require(!ever_deposited);
	
        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.transferFrom(msg.sender, address(this), allowance);

        _deposited = allowance;
    }

    // v1
    function withdraw(uint amount) external {
        require (amount <= token.balanceOf(address(this)));
	
        token.transfer(msg.sender, amount);

        _sent += amount;	
    }

    // p1
    function invariant() public view {
        assert(_sent <= _deposited);
    }

}
