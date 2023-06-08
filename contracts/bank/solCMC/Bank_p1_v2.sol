//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;
    uint totalBalance;

    receive() external payable {
        /* pre-conditions */
        require(totalBalance >= balances[msg.sender]);

        /* body start */
        balances[msg.sender] += msg.value;
        totalBalance += msg.value;
        /* body end */

        /* post-conditions */
        assert(totalBalance >= balances[msg.sender]);
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;
        totalBalance -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: 0.2s
// ----
