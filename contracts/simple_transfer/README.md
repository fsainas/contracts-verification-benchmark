# Simple Transfer

## Specification

The contract has an initial balance, which consists of the
amount of ETH paid to the constructor,
plus the balance of the address of the contract before deployment.
Besides the constructor,
the contract has a `withdraw(amount)` function that transfers the
specified `amount` of ETH to the caller.

## Properties

- **p1**: the overall sent amount does not exceed the initial deposit
- **p2**: the contract balance is monotonically decreasing
- **p3**: the contract balance is decreased by `amount` after a successful `withdraw(amount)`

## Versions

- **v1**: conformant to specification
- **v2**: contract is [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol)


## Experiments

### SolCMC

|        | **p1**             | **p2**             |
| ------ | ------------------ | ------------------ |
| **v1** | :x:                | :x:                |
| **v3** |                    | :heavy_check_mark: |
