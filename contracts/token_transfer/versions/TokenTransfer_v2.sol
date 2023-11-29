// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";
import "./lib/SafeERC20.sol";


/// @custom:version safe IERC20 interactions by using [SafeERC20.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol) (OpenZeppelin)
contract TokenTransfer {
    using SafeERC20 for IERC20;

    IERC20 token;
    bool ever_deposited;
    
    
    // ghost variables
    uint _count_deposit;

    constructor(IERC20 token_) {
        token = token_;
    }

    function deposit() external {
        require(!ever_deposited);

        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.safeTransferFrom(msg.sender, address(this), allowance);
        
        _count_deposit += 1;	
    }

    function withdraw(uint amount) external {
        token.safeTransfer(msg.sender, amount);
    }
}
