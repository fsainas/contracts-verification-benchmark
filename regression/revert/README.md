# Revert

## Specification
The contract `Revert` has a function `f` that takes as input a bool `b` and a uint `a`. If `b` is true, the function calls `revert()`, otherwise it sets the value of `c` to `a + 1` and then increments or decrements `c` based on the value of `b`.
```
function f(bool b, uint a) public {
    require(a <= 256);
    x = a;
    if (b)
        revert();
    c = a + 1;
    if (b)
        c--;
    else
        c++;
}
```

## Properties
- **c-equals-a**: `c` is equal to `a` at the end of function `f`

## Ground truth
|        | c-equals-a |
|--------|------------|
| **v1** | 0[^1]      |
 
[^1]: The condition is always false: if `b` is true, `revert()` is called and the assertion is never reached; otherwise, `c` is set to `a+1` and then incremented by one.

## Experiments
### SolCMC
#### Z3
|        | c-equals-a |
|--------|------------|
| **v1** | TN!        |
 

#### ELD
|        | c-equals-a |
|--------|------------|
| **v1** | TN!        |
 


### Certora
|        | c-equals-a |
|--------|------------|
| **v1** | TN         |
 

