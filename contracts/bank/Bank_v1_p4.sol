//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint) balances;

    // ghost variables
    uint _prev_balance;     // balance of the contract minus balances[msg.sender]

    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

    function invariant(uint amount) public {
        _prev_balance = balances[msg.sender];
        withdraw(amount);
        assert(_prev_balance > balances[msg.sender]);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: n/a
// ----
