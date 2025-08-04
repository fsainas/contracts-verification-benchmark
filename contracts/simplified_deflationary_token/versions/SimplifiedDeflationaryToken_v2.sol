// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @custom:version the deflationary property is not well implemented, when we make a transfer with less than 10 tokens, no fees are charged.
contract SimplifiedDeflationaryToken {
    mapping(address => uint256) public balances;
    mapping(address => bool) public isExcludedFromFee;

    uint256 public totalSupply = 1000000 * (10**18);
    uint256 public transactionFeePercent = 10;

    address public owner;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply;
        isExcludedFromFee[owner] = true;
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 fee = 0;
        if (!isExcludedFromFee[msg.sender]) {
            fee = calculateFee(amount);
            balances[owner] += fee;
        }

        balances[msg.sender] -= amount;
        balances[to] += (amount - fee);

        emit Transfer(msg.sender, to, amount);

        return true;
    }

    function calculateFee(uint256 amount) public view returns (uint256) {
        return (amount * transactionFeePercent) / 100;
    }

    function excludeFromFee(address account) public {
        require(msg.sender == owner, "Only owner can exclude from fee");
        isExcludedFromFee[account] = true;
    }

    function includeInFee(address account) public {
        require(msg.sender == owner, "Only owner can include in fee");
        isExcludedFromFee[account] = false;
    }

    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
}