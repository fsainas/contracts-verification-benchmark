//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint) balances;

    // ghost variables
    uint _total_balance;    // total balance of the contract
    uint _prev_balance;     // balance of the contract minus balances[msg.sender]
    uint _post_balance;

    receive() external payable {
        balances[msg.sender] += msg.value;
        _total_balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;
        _total_balance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

    function invariant(uint amount) public {
        _prev_balance = _total_balance - balances[msg.sender];
        withdraw(amount);
        _post_balance = _total_balance - balances[msg.sender];
        assert(_prev_balance <= _post_balance);     
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: n/a
// ----
