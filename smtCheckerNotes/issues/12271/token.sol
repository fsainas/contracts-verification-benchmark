// SPDX-License-Identifier: MIT
pragma solidity >=0.8.10;

contract Token {
    mapping(address => uint256) private balanceOf;
    uint256 private totalSupply;

    constructor(uint256 totalSupply_) {
        balanceOf[msg.sender] = totalSupply_;
        totalSupply = totalSupply_;
    }

    function transfer(address recipient, uint256 amount) public {
        require(balanceOf[msg.sender] >= amount);
        uint sumPrev = balanceOf[msg.sender] + balanceOf[recipient];
        balanceOf[msg.sender] -= amount;
		balanceOf[recipient] += amount;
		uint sumPost = balanceOf[msg.sender] + balanceOf[recipient];
		assert(sumPrev == sumPost);
    }

    function rule_maxBalanceLessThanTotalSupply(address account) external view {
        assert(balanceOf[account] <= totalSupply);          // CHC: Assertion violation might happen here
    }
}
