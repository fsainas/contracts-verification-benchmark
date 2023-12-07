# Bank
## Specification
The Bank contract is designed to accepts deposits and withdrawals from any address. When a deposit is made, the corresponding amount is added to the account balance of the depositing address. These balances are maintained using a mapping function within the contract. To withdraw funds, a depositor can call the withdraw function of the Bank contract with a specified amount. The contract verifies that the depositor has sufficient funds in their account and then initiates a transfer of the specified amount to the depositor`s address.

## Properties
- **p1**: after a deposit, the total balance of the contract is still greater than or equal to the balance of the account that made the deposit.
- **p2**: after a deposit, if the amount deposited is greater than 0, the balance of the address who made the deposit is increased.
- **p3**:  the only way to decrease the balance of the contract is by calling `withdraw()`.
- **p4**: after a withdrawal, the balance of `msg.sender` is decreased by `amount`.
- **p5**: `withdraw()` does not revert if the sender calls it with an `amount` value less than or equal to their balance in the bank contract.
- **p6**: a user cannot withdraw more than what is currently in their bank balance.

## Versions
- **v1**: conformant to specification
- **v2**: no `amount > 0` check in `withdraw()`
- **v3**: no `amount <= balances[msg.sender]` check and `balances[msg.sender]` is decremented by `amount - 1` in `withdraw()`

## Ground truth
|        | p1  | p2  | p3  | p4  | p5  | p6  |
|--------|-----|-----|-----|-----|-----|-----|
| **v1** | 1   | 1   | 1   | 1   | 1   | 1   |
| **v2** | 1   | 1   | 1   | 1   | 1   | 1   |
| **v3** | 1   | 1   | 1   | 0   | 1   | 0   |

## Experiments

### SolCMC
|        | p1  | p2  | p4  | p6  |
|--------|-----|-----|-----|-----|
| **v1** | TP! | TP! | FN  | TP! |
| **v2** | TP! | TP! | FN  | TP! |
| **v3** | TP! | TP! | TN! | TN! |

### Certora
|        | p1  | p2  | p3  | p4  | p6  |
|--------|-----|-----|-----|-----|-----|
| **v1** | FN! | TP! | TP! | TP! | TP! |
| **v2** | FN! | TP! | TP! | TP! | TP! |
| **v3** | FN! | TP! | TP! | TN! | TN! |