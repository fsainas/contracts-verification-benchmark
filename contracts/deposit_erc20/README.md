# Deposit (ERC20)

## Specification

This contract implements the same functionality of
[SimpleTransfer](../simple_transfer), but operates on ERC20 tokens instead of
ETH. The contract `constructor` takes the token address as a parameter. The
`deposit` function allows the sender to deposit token units into the contract;
it can be called only once. Before calling `deposit`, the depositor must
approve that the amount they want to deposit can be spent by the contract: if
so, the entire allowance is transferred to the contract. 

With ERC20 tokens, it is easier to increase the contract balance without the
contract being able to notice or prevent it, but since this is also possible
with ETH, the behavior can be considered comparable for the purposes of these
tests.


## Properties

- **p1**: `deposit()` can only be called once.

## Versions

- **v1**: conformant to specification.
- **v2**: safe IERC20 interactions by using
  [`SafeERC20.sol`](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol)
  (OpenZeppelin)


## Experiments

### SolCMC

|        | p1  |
| ------ | --- |
| **v1** | TP  |
| **v2** | TP  |   

### Certora

|        | p1  |
| ------ | --- |
| **v1** | TP  |
| **v2** | TP  |
