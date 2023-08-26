// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version Very very cool version, the first of all.
contract Caller {
    uint data;

    function callyourself() public {
        msg.sender.call("");
    }

}