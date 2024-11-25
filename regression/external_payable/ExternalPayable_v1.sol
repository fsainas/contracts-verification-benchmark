//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/external_call_with_value_1.sol
pragma solidity ^0.8.25;

interface I {
	function f() external payable;
}

contract ExternalPayable {
	function g(I i) public {
		require(address(this).balance == 100);
		i.f{value: 10}();
	}

	function balanceOf(address a) public view returns (uint) {
		return a.balance;
	}
}