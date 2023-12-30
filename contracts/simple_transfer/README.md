# Simple Transfer

## Specification
The contract has an initial balance, which consists of the amount of ETH paid to the constructor, plus the balance of the address of the contract before deployment. The contract has a `withdraw` function that transfers an `amount` of ETH (specified as a parameter) to the caller.

## Properties
- **p1**: the overall withdrawn amount does not exceed the initial deposit. This property should always be false, since a contract can receive ETH when its address is specified in a coinbase transaction or in a `self-destruct`.
- **p2**: the contract balance is decreased by the `amount` after a successful `withdraw(amount)`.
- **p3**: after a successful `withdraw(amount)`, the balance of the transaction sender is increased by `amount` ETH.
- **p4**: a transaction `withdraw(amount)` is not reverted whenever the `amount` does not exceed the contract balance.
- **p5**: any user at any time can obtain the full balance of the contract.

## Versions
- **v1**: reentrant `withdraw`.
- **v2**: non-reentrant `withdraw`, using [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol).
- **v3**: `withdraw` transfers to `address(0)` instead of `msg.sender`.
- **v4**: `withdraw` transfers `amount-1` instead of `amount`.
- **v5**: `withdraw` requires a balance of at least `amount+1` instead of `amount`.

## Ground truth
|        | p1    | p2    | p3    | p4    | p5    |
|--------|-------|-------|-------|-------|-------|
| **v1** | 0     | 0     | 0     | 0     | 1     |
| **v2** | 0     | 1     | 1     | 0     | 1     |
| **v3** | 0     | 1     | 0     | 1     | 0     |
| **v4** | 0     | 0     | 0     | 0     | 0     |
| **v5** | 0     | 1     | 1     | 0     | 0     |

## Experiments

### SolCMC
|        | p1    | p2    | p3    | p4    | p5    |
|--------|-------|-------|-------|-------|-------|
| **v1** | TN!   | TN    | TN    | TN!   | ND    |
| **v2** | TN!   | FN    | FN    | TN!   | ND    |
| **v3** | TN!   | FN    | TN    | FN!   | ND    |
| **v4** | TN!   | TN    | TN    | TN!   | ND    |
| **v5** | TN!   | FN    | FN    | TN!   | ND    |

### Certora
|        | p1    | p2    | p3    | p4    | p5    |
|--------|-------|-------|-------|-------|-------|
| **v1** | TN!   | TN!   | TN!   | TN!   | ND    |
| **v2** | TN!   | FN!   | FN!   | TN!   | ND    |
| **v3** | TN!   | FN!   | TN!   | FN!   | ND    |
| **v4** | TN!   | TN!   | TN!   | TN!   | ND    |
| **v5** | TN!   | FN!   | FN!   | TN!   | ND    |
 
