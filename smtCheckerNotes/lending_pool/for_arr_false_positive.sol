pragma solidity >=0.8.0;

contract C {
    uint256 public n;
    address[] public res_arr;   // arr -> res_arr

    function f(address _adr) public {
       
        bool d = false;         // b -> d
        for(uint256 r; r < n; r++) {
            require(r < res_arr.length);
            require(r < n);
            assert(n == res_arr.length);    // CHC: Assertion violation might happen here
            if(res_arr[r] == _adr) {
                d = true;
            }
        }

        require(!d);

        res_arr.push(_adr);
        n = res_arr.length;

        assert(n == res_arr.length);        // Proved
    }
}

// Warning: CHC: Assertion violation might happen here.
