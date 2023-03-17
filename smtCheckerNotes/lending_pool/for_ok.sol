pragma solidity >=0.8.0;

contract C {
    uint256 public n;
    address[] public arr;

    function f(address _adr) public {
       
        bool b = false;
        for(uint256 r; r < n; r++){
            require(r < arr.length);
            require(r < n);
            assert(n == arr.length);        // Proved
            if(arr[r] == _adr){
                b = true;
            }
        }

        require(!b);

        arr.push(_adr);
        n = arr.length;

        assert(n == arr.length);            // Proved
    }
}
