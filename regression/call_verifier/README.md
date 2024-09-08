# Call Revert

## Specification
The contract has only the function `f` that performs an external call:
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```
The properties `call-failure` and `call-success` should both fail since we cannot know if the call will fail or not.

## Properties
- **call-failure**: the external call fails
- **call-success**: the external call succeeds

## Ground truth
|        | call-failure | call-success |
|--------|--------------|--------------|
| **v1** | 0            | 0            |
 

## Experiments
### SolCMC
#### Z3
|        | call-failure | call-success |
|--------|--------------|--------------|
| **v1** | TN!          | TN!          |
 

#### ELD
|        | call-failure | call-success |
|--------|--------------|--------------|
| **v1** | TN           | TN           |
 


### Certora
|        | call-failure | call-success |
|--------|--------------|--------------|
| **v1** | TN           | TN           |
 

