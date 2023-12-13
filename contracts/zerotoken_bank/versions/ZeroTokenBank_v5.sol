/// @custom:version flat caps on deposits and withdraw.
//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract ZeroTokenBank {
    uint contract_balance;
    mapping (address => uint) balances;
    uint last_action_block;

    function balanceOf(address addr) public view returns (uint) {
        return balances[addr];
    }

    function totalBalance() public view returns (uint) {
        return contract_balance;
    }

    function deposit(uint amount) public {
        require(amount < 200);
        balances[msg.sender] += amount;
        contract_balance += amount;
     
        last_action_block = block.number;
    }

    function withdraw(uint amount) public {
        require(amount <= 100);
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        contract_balance -= amount;
     
        last_action_block = block.number;
    }
}
