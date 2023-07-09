// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract SimpleTransfer {

    constructor () payable {
    }

    // ghost functions 
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
    function getAddressBalance(address addr) public view returns (uint) {
        return addr.balance;
    }

    function withdraw(uint amount) public {
        require(amount <= address(this).balance);

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);	
    }
}
