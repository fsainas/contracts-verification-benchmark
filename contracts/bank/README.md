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

- **p1**: after a deposit, the total balance of the contract is greater than or
  equal to the balance of the account that made the deposit
- **p2**: after a deposit, if the amount deposited is greater than 0, the
  balance of the address who made the deposit is increased
- **p3**: after a withdrawal, the balance of `msg.sender` is decreased
- **p4**: after a withdrawal, the balance of `msg.sender` is decreased by `amount`
- **p5**: after a withdrawal, the total balance is decreased
- **p6**: a user cannot withdraw more than what is currently in their bank balance
- **p7**: `withdraw()` does not revert if the sender calls it with an `amount`
  value less than or equal to their balance in the bank contract.
- **p8**: the only way to decrease the balance of the contract is by calling `withdraw()`

## Versions

- **v1**: conformant to specification
- **v2**: the variable `contractBalance` is used to keep track of the contract
  balance instead of directly accessing `address(this).balance`
- **v3**: no `amount > 0` check in `withdraw()`
- **v4**: no `amount <= balances[msg.sender]` check in `withdraw()`

## Experiments

### SolCMC

|        | p1 | p2 | p3 | p4 | p5 | p6 | p7
| ------ | -- | -- | -- | -- | -- | -- | --
| **v1** | TP | TP | ?  | ?  | ?   
| **v2** | TP | TP | ?  | ?  | ?
| **v3** | 
| **v4** |

### Certora
|        | p1 | p2 | p3 | p4 | p5 | p6 | p7
| ------ | -- | -- | -- | -- | -- | -- | --
| **v1** | TP | TP | TP | TP | FP |
| **v2** | TP | TP | TP | TP | TP |
| **v3** | 
| **v4** |

#### Notes
- Not sure about p5/v1.
