# Bank

## Specification

The Bank contract is designed to accepts deposits and withdrawals from any
address. When a deposit is made, the corresponding amount is added to the
account balance of the depositing address. These balances are maintained using
a mapping function within the contract. To withdraw funds, a depositor can call
the withdraw function of the Bank contract with a specified amount. The
contract verifies that the depositor has sufficient funds in their account and
then initiates a transfer of the specified amount to the depositor's address.

## Properties

- **p1**: after a deposit, the contract balance is greater than the balance
  of the account that made the deposit
- **p2**: after a withdrawal, the balance of `msg.sender` is decreased
- **p3**: after a withdrawal, the balance of `msg.sender` is decreased by `amount`
- **p4**: after a withdrawal, the total balance of the contract, excluding the
  balances of the accounts that have made withdrawals, remains unchanged.
- **p5**: after a withdrawal, the total balance of the contract, excluding the
  balances of the accounts that have made withdrawals, either remains unchanged
  or is increased.
- **p6**: after a withdrawal the balance of the account is decreased

## Versions

- **v1**: conformant to specification
- **v2**: the variable `_contractBalance` is used to keep track of the contract
  balance instead of directly accessing `address(this).balance`
- **v3**: no `amount > 0` check in `withdraw()`
- **v4**: no `amount <= balances[msg.sender]` check in `withdraw()`

## Experiments

### SolCMC

|        | p1 | p2 | p3 | p4 
| ------ | -- | -- | -- | --
| **v1** | TP | ?  | ?  |  
| **v2** | TP |    |    |  

### Certora
|        | p1 | p2 | p3 | p4 
| ------ | -- | -- | -- | --
| **v1** | TP | TP | TP |  
| **v2** | TP |    |    |  
