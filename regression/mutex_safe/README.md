# Mutex

## Specification
The contract `MutexSafe` a mutex modifier that prevents reentrancy:
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

## Properties
- **check-mutex**: contract uses mutexes correctly

## Ground truth
|        | check-mutex |
|--------|-------------|
| **v1** | 1[^1]       |
 
[^1]: All the vulnerable functions are marked as `mutex`, making the contract not vulnerable to reentrancy attacks 

## Experiments
### SolCMC
#### Z3
|        | check-mutex |
|--------|-------------|
| **v1** | TP!         |
 

#### ELD
|        | check-mutex |
|--------|-------------|
| **v1** | FN          |
 


### Certora
|        | check-mutex |
|--------|-------------|
| **v1** | TP!         |
 

