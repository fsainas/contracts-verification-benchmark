//SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.8.2;

contract Bank {

    mapping (address => uint256) accounts;

    // ghost variables
    uint _total_balance;

    receive() external payable { 
        accounts[msg.sender] += msg.value;
        _total_balance += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount <= accounts[msg.sender]);

        accounts[msg.sender] -= amount;
        _total_balance -= amount;

        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
    }

    function invariant() public {
        require(accounts[msg.sender] > 0);
        uint prev_total_balance = _total_balance;
        uint account_balance = accounts[msg.sender];
        withdraw(accounts[msg.sender]);
        assert(prev_total_balance - account_balance == _total_balance);
    }

}
