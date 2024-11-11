//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/control_flow/branches_inside_modifiers_2.sol
pragma solidity ^0.8.14;

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
    }
    function getX() public view returns (uint) {
        return x;
    }
}