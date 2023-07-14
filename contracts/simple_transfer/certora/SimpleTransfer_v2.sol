// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

import "lib/ReentrancyGuard.sol";

contract SimpleTransfer is ReentrancyGuard {

    constructor () payable {
    }

    // ghost functions
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function getAddressBalance(address addr) public view returns (uint) {
        return addr.balance;
    }

    function withdraw(uint amount) public nonReentrant {
        require(amount <= address(this).balance);

	    (bool succ,) = address(0).call{value: amount}("");
        require(succ);
    }
}
