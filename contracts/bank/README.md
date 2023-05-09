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
