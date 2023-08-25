// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

contract Caller is ReentrancyGuard {
    uint data;

    function callyourself() public nonReentrant {
        msg.sender.call("");
    }

    // p1
    function invariant() public {
        uint _balance = address(this).balance;
        callyourself();
        assert(_balance == address(this).balance);
    }
}