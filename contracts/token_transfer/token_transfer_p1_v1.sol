// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./IERC20.sol";

contract TokenTransfer {

    IERC20 token;

    uint sent;
    uint deposited;

    constructor (IERC20 _token) {
        token = _token;
        deposited = token.balanceOf(address(this));
    }

    function withdraw(uint _amount) external {
        require (_amount <= token.balanceOf(address(this)));
        sent += _amount;
        token.transfer(msg.sender, _amount);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }
}
// ====
// SMTEngine: CHC
// Time: 0.12s
// Targets: "all"
// Ext Calls: trusted
// ====
// SMTEngine: CHC
// Time: 0.12s
// Targets: "all"
// Ext Calls: untrusted
// ----
// Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here - line 20
// Warning: CHC: Assertion violation happens here - line 25
