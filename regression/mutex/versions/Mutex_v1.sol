//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/external_calls/call_mutex_unsafe.sol

contract Mutex {
	uint x;

	bool lock;
	modifier mutex {
		require(!lock);
		lock = true;
		_;
		lock = false;
	}

	function set(uint _x) mutex public {
		x = _x;
	}

	function f(address _a) public {
		_a.call("aaaaa");
	}
    
    function getX() public view returns (uint) {
		return x;
	}
}