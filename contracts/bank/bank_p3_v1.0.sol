//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint256) accounts;

    // ghost variables
    uint _total_balance;    // total balance of the contract
    uint _prev_balance;     // balance of the contract minus accounts[msg.sender]
    uint _post_balance;

    receive() external payable {
        accounts[msg.sender] += msg.value;
        _total_balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= accounts[msg.sender]);

        accounts[msg.sender] -= amount;
        _total_balance -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant(uint amount) public {
        _prev_balance = _total_balance - accounts[msg.sender];
        withdraw(amount);
        _post_balance = _total_balance - accounts[msg.sender];
        assert(_prev_balance <= _post_balance);     
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: n/a
// ----
