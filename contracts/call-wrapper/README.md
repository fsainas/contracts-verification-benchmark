# CallWrapper
## Specification
The contract acts as a wrapper to Solidity's `call` function.

## Properties
- **p1**: the contract balance is unchanged after a call to  `callwrap`.
- **p2**: the contract storage is unchanged after a call to `callwrap`.

## Versions
- **v1**: Very very cool version, the first of all.
- **v2**: The second version.
- **v3**: The third version.
- **v4**: The fourth version.
- **v5**: The fifth version.

## Ground truths
|        | p1  | p2  |
|--------|-----|-----|
| **v1** | 0   | 1   |
| **v2** | 0   | 1   |
| **v3** | 0   | 0   |
| **v4** | 0   | 0   |
| **v5** | 0   | 1   |
