# Bank

## Specification
The Bank contract is designed to accepts deposits and withdrawals from any
address. When a deposit is made, the corresponding amount is added to the
account balance of the depositing address. These balances are maintained using
a mapping function within the contract. To withdraw funds, a depositor can call
the withdraw function of the Bank contract with a specified amount. The
contract verifies that the depositor has sufficient funds in their account and
then initiates a transfer of the specified amount to the depositor's address.

### Properties
1. **Withdrawal availability**: after a deposit is made, the address that made the
   deposit must be able to withdraw the amount deposited or the total amount
   deposited at any time.

1. **Withdrawal security**: funds can only be withdrawn from the account that
   deposited them.

## Versions
- **v1**: conformant to specification

## Properties
- **p1**: *TODO*
- **p2**: after a withdrawal, the total balance of the contract, excluding the
  balances of the accounts that have made withdrawals, remains unchanged.
    - **p2.1**: the `_post_total_balance` is update before the external call
- **p3**: after a withdrawal, the total balance of the contract, excluding the
  balances of the accounts that have made withdrawals, either remains unchanged
  or is increased.

## Experiments

|        | **p1** | **p2**     | **p2.1**           | **p3**     |
| ------ | ------ | ---------- | ------------------ | ---------- |
| **v1** |        | :question: | :heavy_check_mark: | :question: |
