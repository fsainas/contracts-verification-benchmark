//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;


/// @custom:version no `amount > 0` check in `withdraw()`
contract Bank {
    mapping (address => uint) balances;

    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        //require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
