# ExternalCallConstructorReentrancy

## Specification
We have the contract `ExternalCallConstructorReentrancy` and the interface `D`.
### D interface
`D` is an interface and it defines an external function `ext` which takes the an `ExternalCallConstructorReentrancy` contract as argument and returns a `uint`.
```
interface D {
	function ext(ExternalCallConstructorReentrancy c) external returns (uint);
}
```

### ExternalCallConstructorReentrancy contract
`ExternalCallConstructorReentrancy` has the function `s` and the constructor.

The function `s` takes a uint value and assigns it to the `x` variable.
```
function s(uint _x) public {
	x = _x;
}
```
The constructor takes a `D` interface and calls the `ext` function of the interface with the current contract as argument.
```
constructor(D d) {
    uint a = d.ext(this);
}
```

## Properties
- **safe-external-call**: external call inside constructor is safe

## Ground truth
|        | safe-external-call |
|--------|--------------------|
| **v1** | 1[^1]              |
 
[^1]: The called function is safe because there is no reentrancy from the constructor.

## Experiments
### SolCMC
#### Z3
|        | safe-external-call |
|--------|--------------------|
| **v1** | TP!                |
 

#### ELD
|        | safe-external-call |
|--------|--------------------|
| **v1** | TP!                |
 


### Certora
|        | safe-external-call |
|--------|--------------------|
| **v1** | FN                 |
 

