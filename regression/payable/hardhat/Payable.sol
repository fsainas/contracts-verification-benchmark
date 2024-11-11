pragma solidity ^0.8.25;

contract Payable {
    receive() external payable{}
	function g(address payable i) public {
		require(address(this).balance == 100);
		i.call{value: 10}("");
	}
	function balanceOf(address a) public view returns (uint) {
		return a.balance;
	}
}