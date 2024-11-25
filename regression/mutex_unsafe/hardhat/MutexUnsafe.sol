pragma solidity ^0.8.25;

contract MutexUnsafe {
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