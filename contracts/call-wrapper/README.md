# Call Wrapper
## Specification
The contract acts as a wrapper to Solidity's `call` function.

## Properties
- **p1**: the contract balance is unchanged after a call to `callwrap`.
- **p2**: the contract storage is unchanged after a call to `callwrap`.

## Versions
- **v1**: reentrant `callwrap`.
- **v2**: non-reentrant `callwrap`.
- **v3**: reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v4**: non-reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v5**: non-reentrant `callwrap` and additional non-reentrant function `modifystorage`.

## Ground truths
|        | p1  | p2  |
|--------|-----|-----|
| **v1** | 0   | 1   |
| **v2** | 0   | 1   |
| **v3** | 0   | 0   |
| **v4** | 0   | 0   |
| **v5** | 0   | 1   |

## Experiments

### SolCMC
|        | p1  | p2  |
|--------|-----|-----|
| **v1** | TN! | TP! |
| **v2** | FP! | TP! |
| **v3** | TN! | TN! |
| **v4** | FP! | FP! |
| **v5** | FP! | TP! |

### Certora
|        | p1  | p2  |
|--------|-----|-----|
| **v1** | TN! | TP! |
| **v2** | FP! | TP! |
| **v3** | TN! | FP! |
| **v4** | FP! | FP! |
| **v5** | FP! | TP! |
