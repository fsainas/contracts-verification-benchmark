pragma solidity ^0.8.25;

contract NoInterveningCalls {
	bool b = true;

    function f() public{}
    function g() public {
        b = false;
    }

    function getB() public view returns (bool) {
        return b;
    }
}