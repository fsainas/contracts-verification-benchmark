# Reentrancy view

## Specification
The contract has two functions `s` and `f`:

The function `s` takes a uint value checks if it is equal to the `x` variable.
```
function s(uint _x) public view {
    x == _x;
}
```

The function `f` performs an external call to the fallback function of the contract at address `a` as the function signature is empty.
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```

This contract is vulnerable to reentrancy attack, however the function `s` is a view function and does not modify the state of the contract. 

## Properties
- **f-reentrancy-view-x**: The value of `x` does not change after the call to `f`

## Ground truth
|        | f-reentrancy-view-x |
|--------|---------------------|
| **v1** | 1                   |
 

## Experiments
### SolCMC
#### Z3
|        | f-reentrancy-view-x |
|--------|---------------------|
| **v1** | TP!                 |
 

#### ELD
|        | f-reentrancy-view-x |
|--------|---------------------|
| **v1** | FN                  |
 


### Certora
|        | f-reentrancy-view-x |
|--------|---------------------|
| **v1** | TP!                 |
 

