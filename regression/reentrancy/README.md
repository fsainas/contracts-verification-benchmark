# Reentrancy

## Specification
The contract has two functions `s` and `f`:

The `s` function takes a uint value and assigns it to the `x` variable.
```
function s(uint _x) public {
	x = _x;
}
```

The `f` function performs an external call to the fallback function of the contract at address `a` as the function signature is empty.
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```

This contract is vulnerable to reentrancy attack: an attacker can deploy a malicious contract that calls the `s` function of the vulnerable contract in the fallback function and modify `x` value. 

## Properties
- **f-reentrancy-x**: The value of x is 0 after the call to `f`

## Ground truth
|        | f-reentrancy-x |
|--------|----------------|
| **v1** | 0[^1]          |
 
[^1]: Because of reentrancy x may not be zero after `f()` is called.

## Experiments
### SolCMC
#### Z3
|        | f-reentrancy-x |
|--------|----------------|
| **v1** | TN!            |
 

#### ELD
|        | f-reentrancy-x |
|--------|----------------|
| **v1** | TN             |
 


### Certora
|        | f-reentrancy-x |
|--------|----------------|
| **v1** | TN             |
 

