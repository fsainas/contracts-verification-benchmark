// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

import "./IERC20.sol";

contract TokenTransfer {

    IERC20 token;

    uint sent;
    uint deposited;
    uint balance;

    constructor (IERC20 _token, uint _amount) {
        token = _token;
        token.approve(msg.sender, _amount);
        token.transferFrom(msg.sender, address(this), _amount);
        balance = token.balanceOf(address(this));
        deposited = balance;
    }

    function withdraw(uint _amount) external {
        require (_amount <= balance);
        sent += _amount;
        balance -= _amount;
        token.transfer(msg.sender, _amount);
    }

    function invariant() public view {
        assert(sent <= deposited);
    }

}
// ====
// SMTEngine: CHC
// Time: 1.56s
// Targets: "all"
// Ext Calls: untrusted
// ----
