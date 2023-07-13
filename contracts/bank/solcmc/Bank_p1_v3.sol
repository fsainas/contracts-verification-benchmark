//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) balances;

    // p1
    receive() external payable {
        /* pre-conditions */
        require(address(this).balance - msg.value >= balances[msg.sender]);

        /* body start */
        balances[msg.sender] += msg.value;
        /* body end */

        /* post-conditions */
        assert(address(this).balance >= balances[msg.sender]);
    }

    // v3
    function withdraw(uint amount) public {
        require(amount > 0);
        //require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount - 1;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
