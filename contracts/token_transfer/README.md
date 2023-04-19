# Token Transfer

## Specification
Token Transfer is similar to Simple Transfer, but operates with ERC20 tokens
instead of ethers. It is initialized by passing the token address and the
initial amount to the `constructor()`. The initial token balance is the one of
the contract address at deployment time.

The `deposited` variable keeps track of the total amount ever deposited to the
contract, it should never be decremented. Instead, the `sent` variable keeps
track of the total amount sent outside the contract and it should never be
incremented.

## Versions
- **v1**: conformant to specification;
- **v2**: instead of accessing `token.balanceOf(address(this))` directly, the `balance`
  variable is used to keep track of the balance. 

## Invariants
- **p1**: amount sent does not exceed deposit

## Experiments

|      | p1                 |
| ---- | ------------------ |
|**v1**| :x:                |
|**v2**| :heavy_check_mark: |
