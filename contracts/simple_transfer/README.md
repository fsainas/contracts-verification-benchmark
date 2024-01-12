# Simple Transfer
## Specification
The contract has an initial balance, which consists of the amount of ETH paid to the constructor, plus the balance of the address of the contract before deployment. The contract has a `withdraw` function that transfers an `amount` of ETH (specified as a parameter) to the caller.

## Properties
- **always-deplatable**: any user at any time can obtain the full balance of the contract.
- **rel-le-init-bal**: the overall withdrawn amount does not exceed the initial deposit.
- **wd-contract-bal**: the contract balance is decreased by the `amount` after a successful `withdraw(amount)`.
- **wd-not-revert**: a transaction `withdraw(amount)` is not reverted whenever the `amount` does not exceed the contract balance.
- **wd-sender-bal**: after a successful `withdraw(amount)`, the balance of the transaction sender is increased by `amount` ETH.

## Versions
- **v1**: reentrant `withdraw`.
- **v2**: non-reentrant `withdraw`, using [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol).
- **v3**: `withdraw` transfers to `address(0)` instead of `msg.sender`.
- **v4**: `withdraw` transfers `amount-1` instead of `amount`.
- **v5**: `withdraw` requires a balance of at least `amount+1` instead of `amount`.

## Ground truth
|        | always-deplatable | rel-le-init-bal   | wd-contract-bal   | wd-not-revert     | wd-sender-bal     |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | 1                 | 0[^1]             | 0                 | 0                 | 0                 |
| **v2** | 1                 | 0                 | 1                 | 0                 | 1                 |
| **v3** | 0                 | 0                 | 1                 | 1                 | 0                 |
| **v4** | 0                 | 0                 | 0                 | 0                 | 0                 |
| **v5** | 0                 | 0                 | 1                 | 0                 | 1                 |
 
[^1]: This property should always be false, since a contract can receive ETH when its address is specified in a coinbase transaction or in a `self-destruct`.

## Experiments

### SolCMC
|        | always-deplatable | rel-le-init-bal   | wd-contract-bal   | wd-not-revert     | wd-sender-bal     |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | ND                | TN!               | TN                | TN!               | TN                |
| **v2** | ND                | TN!               | FN                | TN!               | FN                |
| **v3** | ND                | TN!               | FN                | FN!               | TN                |
| **v4** | ND                | TN!               | TN                | TN!               | TN                |
| **v5** | ND                | TN!               | FN                | TN!               | FN                |

### Certora
|        | always-deplatable | rel-le-init-bal   | wd-contract-bal   | wd-not-revert     | wd-sender-bal     |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | ND                | TN!               | TN!               | TN!               | TN!               |
| **v2** | ND                | TN!               | FN!               | TN!               | FN!               |
| **v3** | ND                | TN!               | FN!               | FN!               | TN!               |
| **v4** | ND                | TN!               | TN!               | TN!               | TN!               |
| **v5** | ND                | TN!               | FN!               | TN!               | FN!               |
