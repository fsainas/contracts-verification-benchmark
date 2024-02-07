# Deposit (ETH)

## Specification
The contract accepts a single deposit of ETH through the constructor. The function `withdraw(amount)` can be called by anyone to transfer `amount` ETH to the transaction sender.

## Properties
- **always-depletable**: any user (EOA) at any time can fire a transaction to receive the full balance of the contract.
- **wd-contract-bal**: the contract balance is decreased by `amount` after a successful `withdraw(amount)`.
- **wd-leq-init-bal**: the overall withdrawn amount does not exceed the initial deposit.
- **wd-not-revert**: a transaction `withdraw(amount)` is not reverted whenever the `amount` does not exceed the contract balance.
- **wd-sender-rcv**: after a successful `withdraw(amount)`, the balance of the transaction sender is increased by `amount` ETH.
- **wd-sender-rcv-EOA**: after a successful `withdraw(amount)` originated by an EOA, the balance of the transaction sender is increased by `amount` ETH.

## Versions
- **v1**: reentrant `withdraw`.
- **v2**: non-reentrant `withdraw`.
- **v3**: non-reentrant `withdraw` transfers to `address(0)` instead of `msg.sender`.
- **v4**: non-reentrant `withdraw` transfers `amount-1` instead of `amount`.
- **v5**: non-reentrant `withdraw` requires a balance of at least `amount+1` instead of `amount`.
- **v6**: non-reentrant `withdraw` with blacklist.
- **v7**: non-reentrant `withdraw` with whitelist.
- **v8**: `withdraw` callable only by EOAs.

## Ground truth
|        | always-depletable | wd-contract-bal   | wd-leq-init-bal   | wd-not-revert     | wd-sender-rcv     | wd-sender-rcv-EOA |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | 1                 | 0[^1]             | 0[^2]             | 0                 | 0[^3]             | 1                 |
| **v2** | 1                 | 0                 | 0                 | 0                 | 0                 | 1                 |
| **v3** | 0                 | 0                 | 0                 | 1                 | 0                 | 0                 |
| **v4** | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 |
| **v5** | 0                 | 0                 | 0                 | 0                 | 0                 | 1                 |
| **v6** | 0                 | 0                 | 0                 | 0                 | 0                 | 1                 |
| **v7** | 0                 | 0                 | 0                 | 0                 | 0                 | 1                 |
| **v8** | 1                 | 0                 | 0                 | 1                 | 1                 | 1                 |
 
[^1]: A reentrant call to `withdraw` can remove more ETH than the specified `amount`.
[^2]: This property should always be false, since the contract can receive ETH when its address is specified in a coinbase transaction or in a `s-leq-destruct`.
[^3]: `msg.sender` can be an untrusted contract that transfer the received ETH to another account.

## Experiments
### SolCMC
#### Z3
|        | always-depletable | wd-contract-bal   | wd-leq-init-bal   | wd-not-revert     | wd-sender-rcv     | wd-sender-rcv-EOA |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | ND                | UNK               | TN!               | ND                | TN!               | FN!               |
| **v2** | ND                | UNK               | TN!               | ND                | TN!               | FN!               |
| **v3** | ND                | UNK               | TN!               | ND                | TN!               | TN!               |
| **v4** | ND                | TN!               | TN!               | ND                | TN!               | TN!               |
| **v5** | ND                | UNK               | TN!               | ND                | TN!               | FN!               |
| **v6** | ND                | UNK               | TN!               | ND                | TN!               | FN!               |
| **v7** | ND                | UNK               | TN!               | ND                | TN!               | FN!               |
| **v8** | ND                | UNK               | TN!               | ND                | FN!               | FN!               |
 

#### Eldarica
|        | always-depletable | wd-contract-bal   | wd-leq-init-bal   | wd-not-revert     | wd-sender-rcv     | wd-sender-rcv-EOA |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | ND                | TN!               | TN!               | ND                | TN!               | FN!               |
| **v2** | ND                | FP!               | TN!               | ND                | TN!               | FN!               |
| **v3** | ND                | FP!               | TN!               | ND                | TN!               | TN!               |
| **v4** | ND                | TN!               | TN!               | ND                | TN!               | TN!               |
| **v5** | ND                | FP!               | TN!               | ND                | TN!               | FN!               |
| **v6** | ND                | FP!               | TN!               | ND                | TN!               | FN!               |
| **v7** | ND                | FP!               | TN!               | ND                | TN!               | FN!               |
| **v8** | ND                | TN!               | TN!               | ND                | FN!               | FN!               |
 


### Certora
|        | always-depletable | wd-contract-bal   | wd-leq-init-bal   | wd-not-revert     | wd-sender-rcv     | wd-sender-rcv-EOA |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| **v1** | FN                | TN                | TN                | TN                | TN                | FN                |
| **v2** | FN                | TN                | TN                | TN                | TN                | FN                |
| **v3** | TN                | TN                | TN                | FN                | TN                | TN                |
| **v4** | TN                | TN                | TN                | TN                | TN                | TN                |
| **v5** | TN                | TN                | TN                | TN                | TN                | FN                |
| **v6** | TN                | TN                | TN                | TN                | TN                | FN                |
| **v7** | TN                | TN                | TN                | TN                | TN                | FN                |
| **v8** | FN                | TN                | TN                | FN                | FN                | FN                |
 

