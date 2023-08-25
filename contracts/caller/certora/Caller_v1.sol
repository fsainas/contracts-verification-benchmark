// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Caller {
    uint data;

    function callyourself() public {
        msg.sender.call("");
    }

    // ghosts
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function getData() public view returns (uint) {
        return data;
    }
}