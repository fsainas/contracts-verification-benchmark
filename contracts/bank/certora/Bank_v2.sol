//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {
    mapping (address => uint) private balances;
    uint totalBalance;

    receive() external payable {
        totalBalance += msg.value;
        balances[msg.sender] += msg.value;
    }

    function getBalance(address a) public view returns (uint) {
        return balances[a];
    }

    function getContractBalance() public view returns (uint) {
        return totalBalance;
    }

    function getContractAddress() public view returns (address) {
        return address(this);
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
