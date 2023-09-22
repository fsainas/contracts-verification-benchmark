# Zero-token bank

## Specification

The ZeroTokenBank contract is designed to accepts deposits and withdrawals from any
address. When a deposit is made, the corresponding amount is added to the
account balance of the depositing address. These balances are maintained using
a mapping function within the contract. To withdraw funds, a depositor can call
the withdraw function of the Bank contract with a specified amount. The
contract verifies that the depositor has sufficient funds in their account and
then initiates a transfer of the specified amount to the depositor's address.

## Properties

[TRUE > 0.8]
- **p1**: after a successful `deposit(amount)`, the balance entry of `msg.sender` is increased by `amount`.

[TRUE]
- **p2**: after a successful `withdraw(amount)`, the balance entry of `msg.sender` is decreased by `amount`.

[FALSE]
- **p3**: a `deposit(amount)` call never reverts.

[FALSE]
- **p4**: a `withdraw(amount)` call does not revert if `amount` is less or equal to the balance entry of `msg.sender`.

[TRUE]
- **p5**: the only way to increase the balance entry of a user `a` is by calling `deposit` with `msg.sender = a`.

[TRUE]
- **p6**: the only way to decrease the balance entry of a user `a` is by calling `withdraw` with `msg.sender = a`.

[TRUE]
- **p7**: `contract_balance` is always non-negative.

[TRUE]
- **p8**: every balance entry is always non-negative.

[TRUE]
- **p9**: any user can always increase their balance up to its maximum value.

[FALSE]
- **p10**: any user can always increase their balance.

[TRUE]
- **p11**: `contract_balance` is always greater or equal to any balance entry.

[TRUE]
- **p12**. `contract_balance` is always equal to the sum of the balance entries.

[TRUE]
- **p13**: for every user `a`, their balance entry is equal to the sum of all `amount`s in successful `deposit(amount)` with `msg.sender = a` minus those in successful `withdraw(amount)` with `msg.sender = a`. 

[TRUE]
- **p14**: any user can always withdraw their whole balance entry in a single transaction.

[TRUE]
- **p15**: any user can always withdraw their whole balance entry in a finite sequence of transaction.

[TRUE]
- **p16**: for every user `a`, the sum of all `amount`s withdrawn by `a` is less or equal to the sum of all `amount`s deposited by `a`.

[TRUE]
- **p17**: any transaction made by a user will have the same effect when frontrun by a single transaction made by a different user.

[TRUE]
- **p18**: any transaction made by a user will have the same effect when frontrun by a finite sequence of transactions made by different users.


## Versions

- **v1**: direct translation of the specification
- **v2**: no `amount > 0` check in `withdraw()`
- **v3**: no `amount <= balances[msg.sender]` check and `balances[msg.sender]` is decremented by `amount - 1` in `withdraw()`
- **v4**: blacklist
- **v5**: whitelist
- **v6**: timeout
- **v7**: deposit / withdraw with limited amounts

## Experiments

### SolCMC

### Certora

