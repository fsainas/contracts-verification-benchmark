### Storage contract

The contract `Storage` has two functions `f` and `sum`: 

- the function `f` adds the value of `n` to `x`  
    ```
    function f(uint n) public {
        x = x + n;
    }
    ```
- the function `sum` returns the sum of `a + b`.
    ```
    function sum(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
    ```