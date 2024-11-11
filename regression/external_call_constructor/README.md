# ExternalCallConstructor

## Specification
We have two contracts: `ExternalCallConstructor` and `State`.
### State contract
`State` defines a pure function `f` 
- The function `f` takes in input `_x` and if the value is less than `100`, returns `_x`.
```
function f(uint _x) public pure returns (uint) {
    require(_x < 100);
    return _x;
}
```

### ExternalCallConstructor contract
`ExternalCallConstructor` has two variables, `s` and `z`, and the function `f`.
The contract declares a State contract `s` and initializes `z` to the result of `s.f(2)`. The function `f` is empty as it is used only to assert `z` value in SolCMC.
```
State s;
uint z = s.f(2);

function f() public view{}
```

## Properties
- **safe-external-call**: external call to State contract function is safe

## Ground truth
|        | safe-external-call |
|--------|--------------------|
| **v1** | 1[^1]              |
 
[^1]: The called function is safe, however by default, called contracts are considered untrusted by SolCMC and Certora, even when their code is known.

## Experiments
### SolCMC
#### Z3
|        | safe-external-call |
|--------|--------------------|
| **v1** | FN!                |
 

#### ELD
|        | safe-external-call |
|--------|--------------------|
| **v1** | FN!                |
 


### Certora
|        | safe-external-call |
|--------|--------------------|
| **v1** | FN                 |
 

