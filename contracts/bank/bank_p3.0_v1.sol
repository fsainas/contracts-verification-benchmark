//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint256) accounts;

    // ghost variables
    uint _total_balance;    // total balance of the contract

    receive() external payable {
        accounts[msg.sender] += msg.value;
        _total_balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount <= accounts[msg.sender]);

        uint _prev_total_balance = _total_balance - accounts[msg.sender];

        accounts[msg.sender] -= amount;
        _total_balance -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);

        uint _post_total_balance = _total_balance - accounts[msg.sender];

        assert(_prev_total_balance <= _post_total_balance);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// ----
// Does not seem to terminate
