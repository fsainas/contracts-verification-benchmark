// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";
import "./lib/SafeERC20.sol";

contract TokenTransfer {
    using SafeERC20 for IERC20;

    IERC20 token;
    bool ever_deposited;

    constructor(IERC20 token_) {
        token = token_;
    }

    function deposit() external {
        require(!ever_deposited);

        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.safeTransferFrom(msg.sender, address(this), allowance);
    }

    function withdraw(uint amount) external {
        token.safeTransfer(msg.sender, amount);
    }
}
