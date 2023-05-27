//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint) balances;

    receive() external payable { 
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount <= balances[msg.sender]);
        require(amount > 0);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
