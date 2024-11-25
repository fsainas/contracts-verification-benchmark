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
- **z-equals-2**: z is always equal to 2

## Ground truth
|        | z-equals-2 |
|--------|------------|
| **v1** | 1          |
 

## Experiments
### SolCMC
#### Z3
|        | z-equals-2 |
|--------|------------|
| **v1** | FN!        |
 

#### ELD
|        | z-equals-2 |
|--------|------------|
| **v1** | FN!        |
 


### Certora
|        | z-equals-2 |
|--------|------------|
| **v1** | FN         |
 

