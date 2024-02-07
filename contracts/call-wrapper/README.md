# Call Wrapper

## Specification
The contract acts as a wrapper to Solidity's `call` function.

## Properties
- **bal**: the contract balance is unchanged after a call to `callwrap`.
- **stor**: the contract storage is unchanged after a call to `callwrap`.

## Versions
- **v1**: reentrant `callwrap`.
- **v2**: non-reentrant `callwrap`.
- **v3**: reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v4**: non-reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v5**: non-reentrant `callwrap` and additional non-reentrant function `modifystorage`.

## Ground truth
|        | bal   | stor  |
|--------|-------|-------|
| **v1** | 0     | 1     |
| **v2** | 0     | 1     |
| **v3** | 0     | 0     |
| **v4** | 0     | 0     |
| **v5** | 0     | 1     |
 

## Experiments

### SolCMC (Z3)
|        | bal   | stor  |
|--------|-------|-------|
| **v1** | TN!   | TP!   |
| **v2** | FP!   | TP!   |
| **v3** | TN!   | TN!   |
| **v4** | TN!   | TN!   |
| **v5** | FP!   | TP!   |
 
### SolCMC (Eldarica)
|        | bal   | stor  |
|--------|-------|-------|
| **v1** | TN!   | TP!   |
| **v2** | FP!   | TP!   |
| **v3** | TN!   | TN!   |
| **v4** | TN!   | TN!   |
| **v5** | FP!   | TP!   |
 

### Certora
|        | bal   | stor  |
|--------|-------|-------|
| **v1** | TN    | TP!   |
| **v2** | TN    | TP!   |
| **v3** | TN    | FP!   |
| **v4** | TN    | FP!   |
| **v5** | TN    | TP!   |
 

