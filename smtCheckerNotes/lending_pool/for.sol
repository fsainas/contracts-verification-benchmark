// This is part of the original code written by Enrico Piseddu
pragma solidity >=0.7.0 <0.9.0;

contract C {
    uint256 public numberOfReserves;
    address[] public reserves_array;

    function f(address _adr) public {
       
        // check if reserve already exists
        bool reserveAlreadyExists = false;
        for(uint256 r; r<numberOfReserves; r++) {
            require(r < reserves_array.length);         // +
            require(r < numberOfReserves);              // +
            assert(numberOfReserves == reserves_array.length);     // CHC: Assertion violation might happen
            if(reserves_array[r] == _adr) {              // CHC: Out of bounds access might heppen
                reserveAlreadyExists = true;
            }
        }

        require(!reserveAlreadyExists, "Reserve already exists!");

        reserves_array.push(_adr);
        numberOfReserves = reserves_array.length;        // No more overflow error

        assert(numberOfReserves == reserves_array.length);     // CHC: Assertion violation might happen
    }
}
