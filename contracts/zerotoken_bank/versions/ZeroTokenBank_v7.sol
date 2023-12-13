/// @custom:version withdraw locked after 100 rounds from creation.
//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract ZeroTokenBank {
    uint contract_balance;
    mapping (address => uint) balances;
    uint created_block;
    
    constructor() {
        created_block = block.number;
    }

    function balanceOf(address addr) public view returns (uint) {
        return balances[addr];
    }

    function totalBalance() public view returns (uint) {
        return contract_balance;
    }

    function deposit(uint amount) public {
        balances[msg.sender] += amount;
        contract_balance += amount;
    }

    function withdraw(uint amount) public {
        require(block.number - created_block < 200);
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        contract_balance -= amount;
    }
}
