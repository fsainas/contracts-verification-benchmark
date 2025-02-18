// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/ERC20v1.sol";
import "./lib/SafeERC20.sol";

/// @custom:version safe IERC20 interactions by using [SafeERC20.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol) (OpenZeppelin)
contract TokenTransfer {
    using SafeERC20 for ERC20;

    ERC20 token;
    bool ever_deposited;
    
    uint private sent;
    uint initial_deposit;

    // ghost variables
    uint _count_deposit;

    constructor(ERC20 token_) {
        token = token_;
    }

    function deposit() public {
        require(!ever_deposited);

        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.safeTransferFrom(msg.sender, address(this), allowance);

        initial_deposit = token.totalSupply();
    
        _count_deposit += 1;	
    }

    function withdraw(uint amount) public {
        sent += amount;
        token.safeTransfer(msg.sender, amount);
    }
    function getBalance() public view returns (uint) {
        return token.balanceOf(address(this));
    }

    function getAddressBalance(address addr) public view returns (uint) {
        return token.balanceOf(addr);
    }

    function getSent() public view returns (uint) {
        return sent;
    }

    function getInitialDeposit() public view returns (uint) {
        return initial_deposit;
    }

}
