# Token Transfer

## Specification

TokenTransfer implements the same functionality of [SimpleTransfer](../simple_transfer),
but operates on ERC20 tokens instead of ETH.
The contract `constructor` takes the token address as a parameter.
The `deposit` function allows the sender to deposit token units into the contract;
it can be called only once.
Before calling `deposit`, the depositor must approve that the amount they want to deposit
can be spent by the contract:
if so, the entire allowance is transferred to the contract. 

With ERC20 tokens, it is easier to increase the contract balance without the
contract being able to notice or prevent it, but since this is also possible
with ETH, the behavior can be considered comparable for the purposes of these tests.


## Properties

- **p1**: the overall sent amount does not exceed the initial deposit.
- **p2**: `deposit()` can only be called once.


## Versions

- **v1**: conformant to specification.
- **v2**: instead of accessing `token.balanceOf(address(this))` directly, the `balance`
  variable is used to keep track of the balance. 
- **v3**: as *v2*, but `balance` is not decremented after the withdrawal.
- **v4**: as *v2*, but `ever_deposited` is updated after `token.transferFrom()`.
- **v5**: as *v2*, but with safe IERC20 interactions by using
  [`SafeERC20.sol`](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol)
  (OpenZeppelin)


## Experiments

### SolCMC

|      | **p1** | **p2** |
| ---- | ------ | ------ |
|**v1**| TN??   | TP     |
|**v2**| :heavy_check_mark: | |
|**v3**| :x:                | |
|**v4**| :x:                | |
|**v5**| :heavy_check_mark: | |
