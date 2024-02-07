# Deposit (ERC20)
## Specification
This contract implements the same functionality of the [Deposit contract](../deposit_eth), but operates on ERC20 tokens instead of ETH. 

The `constructor` takes the token address as a parameter. 

The `deposit` function allows the sender to deposit an arbitrary number of token units into the contract; it can be called only once. Before calling `deposit`, the depositor must approve that the amount they want to deposit can be spent by the contract: if so, the entire allowance is transferred to the contract.

The function `withdraw(amount)` can be called by anyone to transfer `amount` token units to the transaction sender.

## Properties
- **no-deposit-twice**: `deposit` can only be called once.
- **wd-contract-bal**: the contract token balance is decreased by `amount` after a successful `withdraw(amount)`.
- **wd-leq-init-bal**: the overall withdrawn amount does not exceed the initial deposit.

## Versions
- **v1**: conformant to specification.
- **v2**: safe IERC20 interactions by using [SafeERC20.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol) (OpenZeppelin)

## Ground truth
|        | no-deposit-twice | wd-contract-bal  | wd-leq-init-bal  |
|--------|------------------|------------------|------------------|
| **v1** | 1                | 1                | 0[^1]            |
| **v2** | 1                | 1                | 0                |
 
[^1]: This property should not hold for ERC20 tokens, since one can easily increase the contract balance without the contract being able to notice or prevent it. Since this is also possible with ETH (via coinbase or `selfdestruct` transactions), the behavior is comparable for the purposes of these tests.

## Experiments

### SolCMC
|        | no-deposit-twice | wd-contract-bal  | wd-leq-init-bal  |
|--------|------------------|------------------|------------------|
| **v1** | TP!              | FN!              | TN!              |
| **v2** | TP!              | FN!              | TN!              |

### Certora
|        | no-deposit-twice | wd-contract-bal  | wd-leq-init-bal  |
|--------|------------------|------------------|------------------|
| **v1** | TP!              | FN!              | TN!              |
| **v2** | TP!              | FN!              | TN!              |
