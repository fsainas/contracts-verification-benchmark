//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint256) accounts;

    receive() external payable { 
        accounts[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= accounts[msg.sender]);

        accounts[msg.sender] -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant(uint amount) public {
        uint _prev_balance = accounts[msg.sender];
        withdraw(amount);
        assert(_prev_balance > accounts[msg.sender]);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: n/a
// ----
