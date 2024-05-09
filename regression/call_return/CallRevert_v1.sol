//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_return_1.sol

contract CallRevert {
	uint x;
	function f(address a) public {
		(bool s, bytes memory data) = a.call("");
	}
}