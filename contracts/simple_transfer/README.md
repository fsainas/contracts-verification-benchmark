# Simple Transfer

## Specification

The contract has an initial balance, which consists of the
amount of ETH paid to the constructor,
plus the balance of the address of the contract before deployment.
The contract has a `withdraw` function that transfers an `amount` of ETH
(specified as parameter) to the caller.

## Properties

- **p1**: the overall sent amount does not exceed the initial deposit.
          This property should always be false, since a contract can receive ETH
          when its address is specified in a coinbase transaction or in a `selfdestruct`.
- **p2**: the contract balance is decreased by `amount` after a successful `withdraw(amount)`.
- **p3**: after a successful a transaction `withdraw(amount)`, the balance of the transaction sender
          is increased by `amount` ETH.
- **p4**: a transaction `withdraw(amount)` is not reverted whenever `amount`
          does not exceed the contract balance.

## Versions

- **v1**: reentrant `withdraw`.
- **v2**: non-reentrant `withdraw`, using [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol).
- **v3**: `withdraw` transfers to `address(0)` instead of `msg.sender`.
- **v4**: `withdraw` transfers `amount-1` instead of `amount`.
- **v5**: `withdraw` requires a balance of at least `amount+1` instead of `amount`.

## Experiments

### SolCMC

|        | **p1** | **p2** | **p3** | **p4** |
| ------ | -------|------- |------- |--------| 
| **v1** | TN     | TN     | ?      |        |
| **v2** | TN     | TP     | ?      | FP     |
| **v3** | TN     | TP     | ?      |        |
| **v4** | TN     | TN     | TN     |        |
| **v5** | TN     | TP     | ?      |        |
