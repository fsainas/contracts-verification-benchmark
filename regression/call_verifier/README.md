# Call Verifier

## Specification
The contract has only the function `f` that performs an external call:
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```
The properties `call-failure` and `call-success` should both fail since we cannot know if the call will fail or not.

The property `ex-call-is-made` checks if an external call appened.

## Properties
- **call-failure**: the external call fails
- **call-success**: the external call succeeds
- **ex-call-is-made**: an external call has been performed

## Ground truth
|        | call-failure    | call-success    | ex-call-is-made |
|--------|-----------------|-----------------|-----------------|
| **v1** | 0               | 0               | 1               |
 

## Experiments
### SolCMC
#### Z3
|        | call-failure    | call-success    | ex-call-is-made |
|--------|-----------------|-----------------|-----------------|
| **v1** | TN!             | TN!             | ND              |
 

#### ELD
|        | call-failure    | call-success    | ex-call-is-made |
|--------|-----------------|-----------------|-----------------|
| **v1** | TN!             | TN!             | ND              |
 


### Certora
|        | call-failure    | call-success    | ex-call-is-made |
|--------|-----------------|-----------------|-----------------|
| **v1** | TN              | TN              | TP!             |
 

