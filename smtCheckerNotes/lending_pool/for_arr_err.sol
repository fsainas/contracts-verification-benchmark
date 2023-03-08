pragma solidity >=0.7.0 <0.9.0;

contract C {
    uint256 public n;
    address[] public res_arr;         // this name has some problems

    function f(address _adr) public {
       
        bool reserveAlreadyExists = false;      // long name
        for(uint256 r; r<n; r++) {
            require(r < res_arr.length);
            require(r < n);
            assert(n == res_arr.length);          // Error
            if(res_arr[r] == _adr) {
                reserveAlreadyExists = true;
            }
        }

        require(!reserveAlreadyExists, "Reserve already exists!");

        res_arr.push(_adr);
        n = res_arr.length;

        assert(n == res_arr.length);              // should hold
    }
}

// Warning: CHC: Error trying to invoke SMT solver.
// Warning: CHC: Assertion violation might happen here
