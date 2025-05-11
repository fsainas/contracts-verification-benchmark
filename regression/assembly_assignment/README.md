# Assembly Assignment

## Specification
The contract has only the function `f` that executes inline assembly to assign `2` to `x` and then it returns `x`:
```
function f(uint x) public pure returns (uint) {
    assembly {
        x := 2
    }
    return x;
}
```

The property `f-return-correct-x` should pass since we know the return value.

## Properties
- **f-return-correct-x**: the function `f` returns the correct value of `x` (2).

## Ground truth
|        | f-return-correct-x |
|--------|--------------------|
| **v1** | 1                  |
 

## Experiments
### SolCMC
#### Z3
|        | f-return-correct-x |
|--------|--------------------|
| **v1** | FN!                |
 

#### ELD
|        | f-return-correct-x |
|--------|--------------------|
| **v1** | FN!                |
 


### Certora
|        | f-return-correct-x |
|--------|--------------------|
| **v1** | TP!                |
 

