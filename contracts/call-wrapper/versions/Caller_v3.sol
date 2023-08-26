// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version The third version.
contract Caller {
    uint data;

    function callyourself() public {
        msg.sender.call("");
    }

    function modifystorage(uint newdata) public {
        data = newdata;
    }

}