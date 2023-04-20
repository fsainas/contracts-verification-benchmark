// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./lib/IERC20.sol";
import "./lib/SafeERC20.sol";

contract TokenTransfer {
    using SafeERC20 for IERC20;

    IERC20 token;

    uint sent;
    uint deposited;

    constructor (IERC20 _token, uint _init_amount) {
        token = _token;
        token.safeApprove(msg.sender, _init_amount);
        token.safeTransferFrom(msg.sender, address(this), _init_amount);
        deposited = token.balanceOf(address(this));
    }

    function withdraw(uint _amount) external {
        require (_amount <= token.balanceOf(address(this)));
        sent += _amount;
        token.safeTransfer(msg.sender, _amount);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }

}
// ====
// SMTEngine: CHC
// Time: 3.77s
// Targets: "all"
// Ext Calls: untrusted
// ----
// Warning: Assertion checker does not yet support this expression - line 41 
// Warning: Assertion checker does not yet implement this type of function call - line 185
// Warning: CHC: Error trying to invoke SMT solver - line 29
// Warning: CHC: Assertion violation might happen here - line 29
