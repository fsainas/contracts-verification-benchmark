//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/control_flow/branches_inside_modifiers_1.sol
pragma solidity ^0.8.25;

contract Modifiers {
    uint x;
    modifier m(uint z) {
		uint y = 3;
        if (z == 10)
            x = 2 + y;
        _;
        if (z == 10)
            x = 4 + y;
    }
    function f() m(10) internal {
        x = 3;
    }
    function g() public {
        x = 0;
        f();
    }
}