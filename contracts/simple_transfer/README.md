# Simple Transfer

## Specification
Simple Transfer is created with an initial balance, which consists of the
amount paid to the constructor plus the balance of the address of the contract
before deployment. There is a simple `withdraw()` function that transfers a
specified amount to the caller.

## Versions
- **v1**: conformant to specification
- **v2**: instead of accessing `address(this).balance` directly, the `balance`
  variable is used to keep track of the balance. 
- **v3**: contract is [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/security/ReentrancyGuard.sol)


## Invariants
- **p1**: amount sent does not exceed deposit
- **p2**: `address(this).balance` is decreased after `withdraw()`

## Experiments

|        | p1                 | p2                 |
| ------ | ------------------ | ------------------ |
| **v1** | :x:                | :x:                |
| **v2** | :heavy_check_mark: |                    |
| **v3** |                    | :heavy_check_mark: |
