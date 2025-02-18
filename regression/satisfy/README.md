# Satify

## Specification
### Satisfy contract

The contract `Satisfy` has one function `f` and two uint `r0` and `r1`: 

- the function `f` reverts if `b == r1 * a / r0 && b * r0 == r1 * a` is not true
    ```
    function f(uint a, uint b) public view{
        require(b == r1 * a / r0 && b * r0 == r1 * a, "Error: r1 * a / r0 != b");
    }
    ```

## Properties
- **f-call-not-revert**: There exist values of `a` and `b` that don't make function `f` revert.

## Ground truth
|        | f-call-not-revert |
|--------|-------------------|
| **v1** | 1                 |
 

## Experiments
### SolCMC
#### Z3
|        | f-call-not-revert |
|--------|-------------------|
| **v1** | ND                |
 

#### ELD
|        | f-call-not-revert |
|--------|-------------------|
| **v1** | ND                |
 


### Certora
|        | f-call-not-revert |
|--------|-------------------|
| **v1** | TP                |
 

