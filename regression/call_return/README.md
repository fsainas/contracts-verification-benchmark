# Call Revert

## Specification
The contract has only the `f` function that performs an external call:
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```
The properties `call-revert` and `call-not-revert` should both fail since we cannot know if the call will fail or not: it depends on the called contract if it contains a fallback function or not.

## Properties
- **call-not-revert**: checks if the external call succeeded
- **call-revert**: checks if the external call failed

## Ground truth
|        | call-not-revert | call-revert     |
|--------|-----------------|-----------------|
| **v1** | 0               | 0               |
 

## Experiments
### SolCMC
#### Z3
|        | call-not-revert | call-revert     |
|--------|-----------------|-----------------|
| **v1** | TN!             | TN!             |
 

#### ELD
|        | call-not-revert | call-revert     |
|--------|-----------------|-----------------|
| **v1** | TN              | TN              |
 


### Certora
|        | call-not-revert | call-revert     |
|--------|-----------------|-----------------|
| **v1** | TN              | TN              |
 

