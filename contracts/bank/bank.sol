//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint256) accounts;

    receive() external payable { 
        accounts[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount <= accounts[msg.sender]);

        accounts[msg.sender] -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

}

