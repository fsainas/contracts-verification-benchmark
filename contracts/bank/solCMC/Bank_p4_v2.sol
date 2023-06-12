//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;
    uint totalBalance;

    receive() external payable {
        balances[msg.sender] += msg.value;
        totalBalance += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;
        totalBalance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

    function invariant(uint amount) public {
        uint _senderBalanceBefore = balances[msg.sender];
        withdraw(amount);
        uint _senderBalanceAfter = balances[msg.sender];
        assert(_senderBalanceBefore == _senderBalanceAfter + amount);
    }

}
