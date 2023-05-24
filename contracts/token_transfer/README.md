# Token Transfer

## Specification
Token Transfer is similar to Simple Transfer, but operates with ERC20 tokens
instead of ethers. It is initialized by passing the token address to the
`constructor()`. In contrast to Simple Transfer, the deposit is made after the
deployment with the `deposit()` function. Before calling this function, the
depositor must approve that the amount he or she wants to deposit can be spent
by the contract. The entire allowance is transferred to the contract when
depositing. 

Like in Simple Transfer the deposit can only be made once. 

With ERC20 tokens, it is easier to increase the contract balance without the
contract being able to notice or prevent it, but since this is also possible
with ethers, the behavior can be considered comparable for the purposes of
these tests.

## Versions
- **v1**: conformant to specification;
- **v2**: instead of accessing `token.balanceOf(address(this))` directly, the `balance`
  variable is used to keep track of the balance. 
- **v3**: as *v2*, but `balance` is not decremented after the withdrawal
- **v4**: as *v2*, but `ever_deposited` is updated after `token.transferFrom()`
- **v5**: as *v2*, but with safe IERC20 interactions by using
  [`SafeERC20.sol`](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.3/contracts/token/ERC20/utils/SafeERC20.sol)
  (OpenZeppelin)

## Properties
- **p1**: amount sent does not exceed deposit

## Experiments

|      | p1                 |
| ---- | ------------------ |
|**v1**| :x:                |
|**v2**| :heavy_check_mark: |
|**v3**| :x:                |
|**v4**| :x:                |
|**v5**| :heavy_check_mark: |
