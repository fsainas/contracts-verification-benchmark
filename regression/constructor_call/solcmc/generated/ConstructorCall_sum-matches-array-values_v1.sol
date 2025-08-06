// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ConstructorCall {
    uint256 private sum;

    //macro for length of values
    uint256 private constant LENGHT = 3;

    uint256[] private values;
    
    constructor(uint256[] memory _values) {
        require(_values.length == LENGHT);
        
        for (uint256 i = 0; i < LENGHT; i++) {
            require (_values[i] > 0, "Value must be greater than zero");
            doSum(_values[i]);
        }
    }

    function doSum(uint256 _value) public {
        require(_value > 0); //double require
    
        sum += _value;
        values.push(_value);
    }

    function getSumOfValues() public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < LENGHT; i++) {
            total += values[i];
        }
        return total;
    }
    function invariant()public  view {
        assert (sum == getSumOfValues());
    }

}


