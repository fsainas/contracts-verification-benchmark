//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;

    // p2
    receive() external payable {
        uint _balanceBefore = balances[msg.sender];

        balances[msg.sender] += msg.value;

        uint _balanceAfter = balances[msg.sender];

        assert(!(msg.value > 0) || _balanceBefore < _balanceAfter);
    }

    // v3
    function withdraw(uint amount) public {
        require(amount > 0);
        //require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
