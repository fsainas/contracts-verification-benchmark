pragma solidity >=0.7.0 <0.9.0;

contract C {
    uint256 public n;
    address[] public res_arr;

    function f(address _adr) public {
       
        bool d = false;     // if this is called 'b' the next assert should hold
        for(uint256 r; r<n; r++) {
            require(r < res_arr.length);
            require(r < n);
            assert(n == res_arr.length);    // should hold
            if(res_arr[r] == _adr) {
                d = true;
            }
        }

        require(!d);

        res_arr.push(_adr);
        n = res_arr.length;

        assert(n == res_arr.length);        // should hold
    }
}

// Warning: CHC: Assertion violation might happen here.
