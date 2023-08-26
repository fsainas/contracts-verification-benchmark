// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version The second version.
contract Caller is ReentrancyGuard {
    uint data;

    function callyourself() public nonReentrant {
        msg.sender.call("");
    }

}