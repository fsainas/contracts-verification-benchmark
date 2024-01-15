# Bank
## Specification
The Bank contract stores assets deposited by users, and and pays them out when required. The `deposit` method allows anyone to deposit assets. When a deposit is made, the corresponding amount is added to the account balance of the sender. The `withdraw` method allows the sender to receive any desired amount of assets deposited in their account. The contract checks that the depositor has sufficient funds in their account and then transfers the specified amount to the sender. In this version of the contract, the only asset handled by the contract is the ETH crypto-currency.

## Properties
- **deposit-contract-balance**: after a successful `deposit()`, the ETH balance of the contract is increased by `msg.value`.
- **deposit-not-revert**: a `deposit` call does not revert if  `msg.value` is less or equal to the ETH balance of `msg.sender`.
- **deposit-revert**: a `deposit` call reverts if  `msg.value` is greater than the ETH balance of `msg.sender`.
- **deposit-user-balance**: after a successful `deposit()`, the balance entry of `msg.sender` is increased by `msg.value`.
- **user-balance-dec-onlyif-withdraw**: the only way to decrease the balance entry of a user `a` is by calling `withdraw` with `msg.sender = a`.
- **user-balance-inc-onlyif-deposit**: the only way to increase the balance entry of a user `a` is by calling `deposit` with `msg.sender = a`.
- **withdraw-contract-balance**: after a successful `withdraw(amount)`, the ETH balance the contract is decreased by `amount`.
- **withdraw-not-revert**: a `withdraw(amount)` call does not revert if  `amount` is bigger than zero and less or equal to the balance entry of `msg.sender`.
- **withdraw-revert**: a `withdraw(amount)` call reverts if  `amount` is zero or greater than the balance entry of `msg.sender`.
- **withdraw-user-balance**: after a successful `withdraw(amount)`, the balance entry of `msg.sender` is decreased by `amount`.

## Versions
- **v1**: conformant to specification
- **v2**: no `amount <= balances[msg.sender]` check and `balances[msg.sender]` is decremented by `amount - 1` in `withdraw()`

## Ground truth
|        | deposit-contract-balance         | deposit-not-revert               | deposit-revert                   | deposit-user-balance             | user-balance-dec-onlyif-withdraw | user-balance-inc-onlyif-deposit  | withdraw-contract-balance        | withdraw-not-revert              | withdraw-revert                  | withdraw-user-balance            |
|--------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| **v1** | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                |
| **v2** | 1                                | 1                                | 1                                | 1                                | 1                                | 1                                | 0                                | 1                                | 0                                | 0                                |


## Experiments

### SolCMC
|        | deposit-contract-balance         | deposit-not-revert               | deposit-revert                   | deposit-user-balance             | user-balance-dec-onlyif-withdraw | user-balance-inc-onlyif-deposit  | withdraw-contract-balance        | withdraw-not-revert              | withdraw-revert                  | withdraw-user-balance            |
|--------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| **v1** | FN!                              | ND                               | ND                               | TP!                              | ND                               | ND                               | FN!                              | FN!                              | ND                               | FN!                              |
| **v2** | FN!                              | ND                               | ND                               | TP!                              | ND                               | ND                               | TN!                              | FN!                              | ND                               | TN!                              |


### Certora
|        | deposit-contract-balance         | deposit-not-revert               | deposit-revert                   | deposit-user-balance             | user-balance-dec-onlyif-withdraw | user-balance-inc-onlyif-deposit  | withdraw-contract-balance        | withdraw-not-revert              | withdraw-revert                  | withdraw-user-balance            |
|--------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| **v1** | FN!                              | ND                               | ND                               | TP!                              | TP!                              | TP!                              | FN!                              | FN!                              | TP!                              | TP!                              |
| **v2** | FN!                              | ND                               | ND                               | TP!                              | TP!                              | TP!                              | TN!                              | FN!                              | TN!                              | TN!                              |
 
