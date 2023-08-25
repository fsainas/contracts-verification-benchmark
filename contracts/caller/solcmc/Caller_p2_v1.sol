// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Caller {
    uint data;

    function callyourself() public {
        msg.sender.call("");
    }

    // p2
    function invariant() public {
        uint _data = data;
        callyourself();
        assert(_data == data);
    }
}