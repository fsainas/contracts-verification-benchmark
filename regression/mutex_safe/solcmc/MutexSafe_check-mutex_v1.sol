contract MutexSafe {
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

	function f(address _a) mutex public {
		uint y = x;
		_a.call("aaaaa");
		assert(y == x);
	}
}