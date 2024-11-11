//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/external_call_this_with_value_2.sol
pragma solidity ^0.8.25;

contract ThisPayable {
	function g(uint i) public {
		require(address(this).balance == 100);
		this.h{value: i}();
	}
	function h() external payable {}
	function balanceOf(address a) public view returns (uint) {
		return a.balance;
	}
}