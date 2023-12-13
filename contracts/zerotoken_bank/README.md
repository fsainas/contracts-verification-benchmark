
# Zero-token Bank
## Specification
The ZeroTokenBank contract is designed to accepts deposits and withdrawals from any address. When a deposit is made, the corresponding amount is added to the account balance of the depositing address. These balances are maintained using a mapping function within the contract. To withdraw funds, a depositor can call the withdraw function of the Bank contract with a specified amount. The contract verifies that the depositor has sufficient funds in their account and then initiates a transfer of the specified amount to the depositor's address.

## Properties
- **p1**: after a successful `deposit(amount)`, the balance entry of `msg.sender` is increased by `amount`.
- **p2**: after a successful `withdraw(amount)`, the balance entry of `msg.sender` is decreased by `amount`.
- **p3**: a `deposit(amount)` call never reverts.
- **p4**: a `withdraw(amount)` call does not revert if `amount` is bigger than zero and less or equal to the balance entry of `msg.sender`.
- **p5**: the only way to increase the balance entry of a user `a` is by calling `deposit` with `msg.sender = a`.
- **p6**: the only way to decrease the balance entry of a user `a` is by calling `withdraw` with `msg.sender = a`.
- **p7**: `contract_balance` is always non-negative.
- **p8**: every balance entry is always non-negative.
- **p9**: any user can always increase their balance up to its maximum value with a single transaction.
- **p10**: any user can always increase their balance.
- **p11**: `contract_balance` is always greater or equal to any balance entry.
- **p12**: `contract_balance` is always equal to the sum of the balance entries.
- **p13**: for every user `a`, their balance entry is equal to the sum of all `amount`s in successful `deposit(amount)` with `msg.sender = a` minus those in successful `withdraw(amount)` with `msg.sender = a`.
- **p14**: any user can always withdraw their whole balance entry in a single transaction.
- **p15**: any user can always withdraw their whole balance entry in a finite sequence of transaction.
- **p16**: for every user `a`, the sum of all `amount`s withdrawn by `a` is less or equal to the sum of all `amount`s deposited by `a`.
- **p17**: any transaction made by a user will have the same effect when frontrun by a single transaction made by a different user.
- **p18**: any transaction made by a user will have the same effect when frontrun by a finite sequence of transactions made by different users.

## Versions
- **v1**: compliant with the specification.
- **v2**: does not require withdraw cap.
- **v3**: withdraws wrong amount.
- **v4**: owner cannot withdraw
- **v5**: flat caps on deposits and withdraw.
- **v6**: has to be "pinged" after 10 blocks of inactivity in order to withdraw.
- **v7**: withdraw locked after 100 rounds from creation.

## Ground truth
|        | p1  | p2  | p3  | p4  | p5  | p6  | p7  | p8  | p9  | p10 | p11 | p12 | p13 | p14 | p15 | p16 | p17 | p18 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **v1** | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| **v2** | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| **v3** | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   |
| **v4** | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| **v5** | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   |
| **v6** | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 0   |
| **v7** | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 1   | 1   | 1   | 1   |


## Experiments

### SolCMC
|        | p1  | p2  | p3  | p4  | p7  | p8  | p11 |
|--------|-----|-----|-----|-----|-----|-----|-----|
| **v1** | TP! | TP! | TN! | FN! | TP! | TP! | FN  |
| **v2** | TP! | TP! | TN! | FN! | TP! | TP! | FN  |
| **v3** | TP! | TN! | TN! | FN! | TP! | TP! | TN! |
| **v4** | TP! | TP! | TN! | FN! | TP! | TP! | FN  |
| **v5** | TP! | TP! | TN! | FN! | TP! | TP! | FN  |
| **v6** | TP! | TP! | TN! | TN! | TP! | TP! | FN  |
| **v7** | TP! | TP! | FN! | TN! | TP! | TP! | FN  |

### Certora
|        | p1  | p2  | p3  | p4  | p5  | p6  | p7  | p8  | p9  | p11 | p12 | p14 | p15 | p17 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **v1** | TP! | TP! | TN! | FN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | FN! | FN! | FN! |
| **v2** | TP! | TP! | TN! | FN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | FN! | FN! | FN! |
| **v3** | TP! | TN! | TN! | FN! | TP! | TP! | TP! | TP! | TN! | TN! | FP! | FN! | FN! | TN! |
| **v4** | TP! | TP! | TN! | FN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | FN! | FN! | FN! |
| **v5** | TP! | TP! | TN! | FN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | TN! | FN! | FN! |
| **v6** | TP! | TP! | TN! | TN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | TN! | TN! | TN! |
| **v7** | TP! | TP! | FN! | TN! | TP! | TP! | TP! | TP! | TN! | FN! | TP! | TN! | FN! | FN! |