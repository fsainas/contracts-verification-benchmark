// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";

contract TokenTransfer {

    IERC20 token;

    bool ever_deposited;

    // ghost variables
    uint counter;

    constructor(IERC20 token_) {
        token = token_;
    }

    function deposit() external {
        require(!ever_deposited);
        counter += 1;
        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.transferFrom(msg.sender, address(this), allowance);
    }

    function withdraw(uint amount) external {
        token.transfer(msg.sender, amount);
    }

    function invariant() public view {
        assert(counter <= 1);
    }
    
}
