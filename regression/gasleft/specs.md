The contract `GasLeft` has a function `f` that calls `gasleft` twice so that we can check that the gas left decreases after each call.
```
function f() public {
    uint g = gasleft();
    gasleft();
}
```