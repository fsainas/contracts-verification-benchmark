//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;

    receive() external payable {
        require(address(this).balance - msg.value >= balances[msg.sender]);

        // Function start
        balances[msg.sender] += msg.value;
        // Function end

        assert(address(this).balance >= balances[msg.sender]);
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: 0.2s
// ----
