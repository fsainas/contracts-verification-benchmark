# Storage

## Specification
### Storage contract

The contract `Storage` has two functions `f` and `sum`: 

- the function `f` adds the value of `n` to `x`  
    ```
    function f(uint n) public {
        x = x + n;
    }
    ```
- the function `sum` returns the sum of `a + b`.
    ```
    function sum(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
    ```

## Properties
- **equivalent-operations-same-result**: Two equivalent operations starting in the same initial state should produce the same result.

## Ground truth
|        | equivalent-operations-same-result |
|--------|-----------------------------------|
| **v1** | 1                                 |
 

## Experiments
### SolCMC
#### Z3
|        | equivalent-operations-same-result |
|--------|-----------------------------------|
| **v1** | ND                                |
 

#### ELD
|        | equivalent-operations-same-result |
|--------|-----------------------------------|
| **v1** | ND                                |
 


### Certora
|        | equivalent-operations-same-result |
|--------|-----------------------------------|
| **v1** | TP!                               |
 

