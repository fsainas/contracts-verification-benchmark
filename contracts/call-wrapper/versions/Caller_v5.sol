// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version The fifth version.
contract Caller is ReentrancyGuard {
    uint data;

    function callyourself() public nonReentrant {
        msg.sender.call("");
    }

    function modifystorage(uint newdata) public nonReentrant {
        data = newdata;
    }

}