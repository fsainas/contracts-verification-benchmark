pragma solidity ^0.8.25;

contract TwoModifiers {
    uint x;
    modifier m(uint z) {
		uint y = 3;
        if (z == 10)
            x = 2 + y;
        _;
        if (z == 10)
            x = 4 + y;
    }
    function f() m(10) m(12) internal {
        x = 3;
    }
    function g() public {
        x = 0;
        f();
        assert(x == 7);
    }
}