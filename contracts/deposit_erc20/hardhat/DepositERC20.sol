// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./ERC20v1.sol";

/// @custom:version conformant to specification.
contract TokenTransfer {
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
        token.transferFrom(msg.sender, address(this), allowance);

        initial_deposit = token.totalSupply();

        _count_deposit += 1;	
    }

    function withdraw(uint amount) public {
        sent += amount;
        token.transfer(msg.sender, amount);
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
