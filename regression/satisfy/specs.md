### Satisfy contract

The contract `Satisfy` has one function `f` and two uint `r0` and `r1`: 

- the function `f` reverts if `b == r1 * a / r0 && b * r0 == r1 * a` is not true
    ```
    function f(uint a, uint b) public view{
        require(b == r1 * a / r0 && b * r0 == r1 * a, "Error: r1 * a / r0 != b");
    }
    ```