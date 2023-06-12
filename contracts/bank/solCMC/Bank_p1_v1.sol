//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;

    receive() external payable {
        /* pre-conditions */
        require(address(this).balance - msg.value >= balances[msg.sender]);

        /* body start */
        balances[msg.sender] += msg.value;
        /* body end */

        /* post-conditions */
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