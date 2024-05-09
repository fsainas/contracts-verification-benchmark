# Mutex

## Specification
The contract `Mutex` a mutex modifier that prevents reentrancy:
```
modifier mutex {
    require(!lock);
    lock = true;
    _;
    lock = false;
}
```
The contract has also two functions `set` and `f`. The `set` function sets the value of `x` to the input value `_x`. The `f` function performs an external call to the contract at address `_a`.

The first version of the contract is still vulnerable to reentrancy attacks because `f` function is not marked as `mutex`. 
```
function set(uint _x) mutex public {
    x = _x;
}

function f(address _a) public {
    _a.call("aaaaa");
}
```

The second version of the contract is not vulnerable. All the vulnerable functions must be marked as `mutex` to prevent reentrancy attacks. 
```
function set(uint _x) mutex public {
    x = _x;
}

function f(address _a) mutex public {
    _a.call("aaaaa");
}
```

## Properties
- **check-mutex**: checks that the contract uses mutexes correctly to prevent reentrancy attacks

## Ground truth
|        | check-mutex |
|--------|-------------|
| **v1** | 0           |
| **v2** | 1           |
 

## Experiments
### SolCMC
#### Z3
|        | check-mutex |
|--------|-------------|
| **v1** | TN!         |
| **v2** | TP!         |
 

#### ELD
|        | check-mutex |
|--------|-------------|
| **v1** | TN          |
| **v2** | FN          |
 


### Certora
|        | check-mutex |
|--------|-------------|
| **v1** | FP!         |
| **v2** | TP!         |
 

