# Caller
## Specification
The contract acts as a wrapper to Solidity's `call` function.

## Properties
- **p1**: the contract balance is unchanged after a call to  `callwrap`.
- **p2**: the contract storage is unchanged after a call to `callwrap`.

## Versions
- **v1**: reentrant `callwrap`.
- **v2**: non-reentrant `callwrap`.
- **v3**: reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v4**: non-reentrant `callwrap` and additional reentrant function `modifystorage`.
- **v5**: non-reentrant `callwrap` and additional non-reentrant function `modifystorage`.

## Experiments

### SolCMC

|        | p1  | p2  |
| ------ | --- | --- |
| **v1** | TN  | TP  |
| **v2** | FP  | TP  |
| **v3** | TN  | TP  |
| **v4** | TN  | TP  |
| **v5** | FP  | TP  |

### Certora

|        | p1  | p2  |
| ------ | --- | --- |
| **v1** | TN  | TP  |
| **v2** | TN  | TP  |
| **v3** | TN  | TP  |
| **v4** | TN  | TP  |
| **v5** | TN  | TP  |