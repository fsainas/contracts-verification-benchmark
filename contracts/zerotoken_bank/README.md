# Zero-token Bank

## Specification
The ZeroTokenBank contract accepts deposits and withdrawals from any address. When a deposit is made, the corresponding amount is added to the account balance of the depositing address. These balances are maintained using a mapping within the contract. To withdraw funds, a user can call the withdraw function of the Bank contract with a specified amount. The contract verifies that the depositor has sufficient funds in their account and then initiates a transfer of the specified amount to the depositor's address.

## Properties
- **always-bal-inc**: any user can always increase their balance.
- **always-bal-to-max**: any user can always increase their balance up to its maximum value with a single transaction.
- **always-wd-all-many**: any user can always withdraw their whole balance entry in a finite sequence of transaction.
- **always-wd-all-one**: any user can always withdraw their whole balance entry in a single transaction.
- **bal-dec-onlyif-wd**: the only way to decrease the balance entry of a user `a` is by calling `withdraw` with `msg.sender = a`.
- **bal-inc-onlyif-dep**: the only way to increase the balance entry of a user `a` is by calling `deposit` with `msg.sender = a`.
- **bal-nonneg**: every balance entry is always non-negative.
- **bal-sum-dep-wd**: for every user `a`, their balance entry is equal to the sum of all `amount`s in successful `deposit(amount)` with `msg.sender = a` minus those in successful `withdraw(amount)` with `msg.sender = a`.
- **cbal-eq-sum-bal**: `contract_balance` is always equal to the sum of the balance entries.
- **cbal-ge-bal**: `contract_balance` is always greater or equal to any balance entry.
- **cbal-nonneg**: `contract_balance` is always non-negative.
- **dep-inc-snd-bal**: after a successful `deposit(amount)`, the balance entry of `msg.sender` is increased by `amount`.
- **dep-not-revert**: a `deposit(amount)` call never reverts.
- **frontrun-many**: any transaction made by a user will have the same effect when frontrun by a finite sequence of transactions made by different users.
- **frontrun-one**: any transaction made by a user will have the same effect when frontrun by a single transaction made by a different user.
- **sum-wd-le-sum-dep**: for every user `a`, the sum of all `amount`s withdrawn by `a` is less or equal to the sum of all `amount`s deposited by `a`.
- **wd-dec-snd-bal**: after a successful `withdraw(amount)`, the balance entry of `msg.sender` is decreased by `amount`.
- **wd-not-revert**: a `withdraw(amount)` call does not revert if `amount` is bigger than zero and less or equal to the balance entry of `msg.sender`.

## Versions
- **v1**: compliant with the specification.
- **v2**: does not require withdraw cap.
- **v3**: withdraws wrong amount.
- **v4**: owner cannot withdraw
- **v5**: flat caps on deposits and withdraw.
- **v6**: has to be "pinged" after 10 blocks of inactivity in order to withdraw.
- **v7**: withdraw locked after 100 rounds from creation.

## Ground truth
|        | always-bal-inc     | always-bal-to-max  | always-wd-all-many | always-wd-all-one  | bal-dec-onlyif-wd  | bal-inc-onlyif-dep | bal-nonneg         | bal-sum-dep-wd     | cbal-eq-sum-bal    | cbal-ge-bal        | cbal-nonneg        | dep-inc-snd-bal    | dep-not-revert     | frontrun-many      | frontrun-one       | sum-wd-le-sum-dep  | wd-dec-snd-bal     | wd-not-revert      |
|--------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| **v1** | 0[^1]              | 0[^2]              | 1                  | 1                  | 1[^3]              | 1[^4]              | 1[^5]              | 1                  | 1                  | 1[^6]              | 1[^7]              | 1                  | 0[^8]              | 1                  | 1                  | 1                  | 1                  | 1                  |
| **v2** | 0                  | 0                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0                  | 1                  | 1                  | 1                  | 1                  | 1                  |
| **v3** | 0                  | 0                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0[^9]              | 0[^10]             | 0[^11]             | 1                  | 1                  | 0                  | 0[^12]             | 0[^13]             | 0[^14]             | 0[^15]             | 1                  |
| **v4** | 0                  | 0[^16]             | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0                  | 1                  | 1                  | 1                  | 1                  | 1                  |
| **v5** | 0                  | 0[^17]             | 1                  | 0[^18]             | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0                  | 1                  | 1                  | 1                  | 1                  | 1                  |
| **v6** | 0                  | 0                  | 0[^19]             | 0[^20]             | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0                  | 0[^21]             | 0[^22]             | 1                  | 1                  | 0[^23]             |
| **v7** | 0                  | 0                  | 1                  | 0[^24]             | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 1                  | 0[^25]             |
 
[^1]: balance may be at MAX_UINT
[^2]: only if nobody else has deposited 
[^3]: in all versions parameters are uints
[^4]: in all versions  parameters are uints
[^5]: balance is a map to uints
[^6]: requires inductive reasoning about the sum
[^7]: contract_balance is a uint
[^8]: reverts if overflow
[^9]: balance modified incorrectly in withdraw
[^10]: balance and contract_balance are modified incorrectly in withdraw
[^11]: balance and contract_balance are modified incorrectly in withdraw
[^12]: the incorrect balance change can make it impossible for other users to withdraw
[^13]: the incorrect balance change can make it impossible for other users to withdraw
[^14]: users can withdraw more than deposited
[^15]: balance entry modified by one less than the withdrawn amount
[^16]: the owner cannot increase their balance
[^17]: deposit bounded: requires multiple transactions
[^18]: have to withdraw 100 ETH at a time
[^19]: after 100 blocks it is impossible to withdraw
[^20]: requires two transactions in general: one to wakeup the contract and one to withdraw
[^21]: another user may wake up the contract
[^22]: another user may wake up the contract
[^23]: will revert if inactive for 10 rounds
[^24]: after 100 blocks it is impossible to withdraw
[^25]: will revert if 100 rounds have elapsed

## Experiments
