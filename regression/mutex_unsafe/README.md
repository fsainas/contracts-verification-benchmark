# MutexUnsafe

## Specification
The contract `MutexUnsafe` has a mutex modifier that prevents reentrancy:
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

function f(address _a) public {
    _a.call("aaaaa");
}
```

## Properties
- **check-mutex**: contract uses mutexes correctly

## Ground truth
|        | check-mutex |
|--------|-------------|
| **v1** | 0[^1]       |
 
[^1]: The contract does not use mutexes correctly because function `f` is not marked as `mutex`, making it vulnerable to reentrancy attacks

## Experiments
### SolCMC
#### Z3
|        | check-mutex |
|--------|-------------|
| **v1** | TN!         |
 

#### ELD
|        | check-mutex |
|--------|-------------|
| **v1** | TN!         |
 


### Certora
|        | check-mutex |
|--------|-------------|
| **v1** | FP!         |
 

