//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_with_value_1.sol

contract Payable {
	function g(address payable i) public {
		require(address(this).balance == 100);
		i.call{value: 10}("");
	}
	function balanceOf(address a) public view returns (uint) {
		return a.balance;
	}
}