//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) private balances;

    function getBalance(address a) public view returns (uint) {
        return balances[a];
    }

    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }

    function receiveEth() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
