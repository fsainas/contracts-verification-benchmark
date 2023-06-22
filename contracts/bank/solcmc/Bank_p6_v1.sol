//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;

    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    // v1
    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

    // p6
    function invariant(uint amount) public {
        uint _senderBalanceBefore = balances[msg.sender];
        withdraw(amount);
        assert(amount <= _senderBalanceBefore);
    }

}
