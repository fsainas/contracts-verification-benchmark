// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;
import "./lib/ReentrancyGuard.sol";

/// @custom:version non-reentrant `callwrap` and additional reentrant function `modifystorage`.
contract CallWrapper is ReentrancyGuard {
    uint data;

    function callwrap(address called) public nonReentrant {
        called.call("");
    }

    function modifystorage(uint newdata) public {
        data = newdata;
    }

}