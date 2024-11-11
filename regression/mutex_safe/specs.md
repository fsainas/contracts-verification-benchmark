The contract `MutexSafe` has a mutex modifier that prevents reentrancy:
```
modifier mutex {
    require(!lock);
    lock = true;
    _;
    lock = false;
}
```
The contract has also two functions `set` and `f`. The function `set` sets the value of `x` to the input value `_x`. The function `f` performs an external call to the contract at address `_a`.
```
function set(uint _x) mutex public {
    x = _x;
}

function f(address _a) mutex public {
    _a.call("aaaaa");
}
```