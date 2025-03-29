# Deposit (ERC20)

## Specification
This contract implements the same functionality of the [Deposit contract](../deposit_eth), but operates on ERC20 tokens instead of ETH. 

The `constructor` takes the token address as a parameter. 

The `deposit` function allows the sender to deposit an arbitrary number of token units into the contract; it can be called only once. Before calling `deposit`, the depositor must approve that the amount they want to deposit can be spent by the contract: if so, the entire allowance is transferred to the contract.

The function `withdraw(amount)` can be called by anyone to transfer `amount` token units to the transaction sender.

## Properties
- **always-depletable**: anyone at any time can fire a transaction to receive the full balance of the contract.
- **deposit-deposit-revert**: if `deposit` is called after `deposit` the second call aborts.
- **no-deposit-twice**: `deposit` can only be called once.
- **wd-contract-bal**: the contract token balance is decreased by `amount` after a successful `withdraw(amount)`.
- **wd-leq-init-bal**: the overall withdrawn amount does not exceed the initial deposit.
- **wd-not-revert**: a transaction `withdraw(amount)` is not reverted whenever the `amount` does not exceed the contract balance.
- **wd-sender-rcv**: after a successful `withdraw(amount)`, the balance of the transaction sender is increased by `amount`.

## Versions
- **v1**: conformant to specification.

## Ground truth
|        | always-depletable      | deposit-deposit-revert | no-deposit-twice       | wd-contract-bal        | wd-leq-init-bal        | wd-not-revert          | wd-sender-rcv          |
|--------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| **v1** | 1                      | 1                      | 1                      | 1                      | 0[^1]                  | 1                      | 1                      |
 
[^1]: This property should not hold for ERC20 tokens, since one can easily increase the contract balance without the contract being able to notice or prevent it. Since this is also possible with ETH (via coinbase or `selfdestruct` transactions), the behavior is comparable for the purposes of these tests.

## Experiments
### SolCMC
#### Z3
|        | always-depletable      | deposit-deposit-revert | no-deposit-twice       | wd-contract-bal        | wd-leq-init-bal        | wd-not-revert          | wd-sender-rcv          |
|--------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| **v1** | ND                     | ND                     | ERR                    | FN!                    | TN!                    | ND                     | ND                     |
 

#### ELD
|        | always-depletable      | deposit-deposit-revert | no-deposit-twice       | wd-contract-bal        | wd-leq-init-bal        | wd-not-revert          | wd-sender-rcv          |
|--------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| **v1** | ND                     | ND                     | TP!                    | FN!                    | TN!                    | ND                     | ND                     |
 


### Certora
|        | always-depletable      | deposit-deposit-revert | no-deposit-twice       | wd-contract-bal        | wd-leq-init-bal        | wd-not-revert          | wd-sender-rcv          |
|--------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| **v1** | TP!                    | TP!                    | TP!                    | TP!                    | TN                     | TP!                    | TP!                    |
 

