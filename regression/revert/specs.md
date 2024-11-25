The contract `Revert` has a function `f` that takes as input a bool `b` and a uint `a`. If `b` is true, the function calls `revert()`, otherwise it sets the value of `c` to `a + 1` and then increments or decrements `c` based on the value of `b`.
```
function f(bool b, uint a) public {
    require(a <= 256);
    x = a;
    if (b)
        revert();
    c = a + 1;
    if (b)
        c--;
    else
        c++;
}
```