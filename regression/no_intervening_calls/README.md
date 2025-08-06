# No Intervening Calls

## Specification
The `NoInterveningCalls` contract manages a boolean state variable `b` with two functions:

- `f()`: A no-op function that performs no state changes.
- `g()`: A function that modifies the state by setting `b` to `false`.

When `f()` is called two times in a row and `g()` is not called, the value of `b` should not change.

## Properties
- **explicit-g-call**: `b` is `true` after `g()` is explicitly called between the two `f()` calls in the CVL rule.
- **no-explicit-g-call**: `b` is `true` after two consecutive calls to `f()` in the CVL rule, without any intervening calls to `g()`.

## Ground truth
|        | explicit-g-call    | no-explicit-g-call |
|--------|--------------------|--------------------|
| **v1** | 0                  | 1                  |
 

## Experiments
### SolCMC
#### Z3
|        | explicit-g-call    | no-explicit-g-call |
|--------|--------------------|--------------------|
| **v1** | TN!                | TP!                |
 

#### ELD
|        | explicit-g-call    | no-explicit-g-call |
|--------|--------------------|--------------------|
| **v1** | TN!                | TP!                |
 


### Certora
|        | explicit-g-call    | no-explicit-g-call |
|--------|--------------------|--------------------|
| **v1** | TN                 | TP!                |
 

