// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./IERC20.sol";

contract TokenTransfer {

    IERC20 token;

    uint sent;
    uint deposited;

    constructor (IERC20 _token, uint _amount) {
        token = _token;
        token.approve(msg.sender, _amount);
        token.transferFrom(msg.sender, address(this), _amount);
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
// Time: 1.51s
// Targets: "all"
// Ext Calls: untrusted
// ----
// Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here - line 22
// Warning: CHC: Assertion violation happens here - line 27
