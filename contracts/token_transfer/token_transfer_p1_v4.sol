// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";

contract TokenTransfer {

    IERC20 token;

    bool ever_deposited;
    uint balance;

    // ghost variables
    uint _sent;
    uint _deposited;
    
    // The deposits can be made by interacting with the ERC20 contract
    constructor(IERC20 token_) {
        token = token_;
    }

    // This is the only valid deposit method
    function deposit() external {
        require(!ever_deposited);
        uint allowance = token.allowance(msg.sender, address(this));
        token.transferFrom(msg.sender, address(this), allowance);
        ever_deposited = true;
        balance += allowance;
        _deposited = balance;
    }

    function withdraw(uint amount) external {
        require (amount <= balance);
        _sent += amount;
        balance -= amount;
        token.transfer(msg.sender, amount);
    }

    function invariant() public view {
        assert(_sent <= _deposited);
    }

}

// ====
// SMTEngine: CHC
// Time: 18.33s
// Targets: "all"
// Ext Calls: untrusted
// ----
// Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here - line 28
// Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here - line 34
// Warning: CHC: Assertion violation happens here - line 40
