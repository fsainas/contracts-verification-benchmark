// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract NonLinearMult {
    uint private constant c = 3;
    uint private a;
    uint private b;
    constructor(uint _a) {
        a = _a;
        b = c;
    }

    function getAB() public view returns (uint){
        return a * b;
    }
     
    function getAC() public view returns (uint) {
        return a * c;
    }

}


