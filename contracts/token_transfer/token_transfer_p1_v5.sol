// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";
import "./lib/SafeERC20.sol";

contract TokenTransfer {
    using SafeERC20 for IERC20;

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
        ever_deposited = true;
        uint allowance = token.allowance(msg.sender, address(this));
        token.safeTransferFrom(msg.sender, address(this), allowance);
        balance += allowance;
        _deposited = balance;
    }

    function withdraw(uint amount) external {
        require (amount <= balance);
        _sent += amount;
        balance -= amount;
        token.safeTransfer(msg.sender, amount);
    }

    function invariant() public view {
        assert(_sent <= _deposited);
    }

}

// ====
// SMTEngine: CHC
// Time: 123.34s
// Targets: "all"
// Ext Calls: untrusted
// ----
// Warning: Assertion checker does not yet support this expression - lib/Address.sol - line 41
// Warning: Assertion checker does not yet implement this type of function call - lib/Address.sol - line 185
