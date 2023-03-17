#
[Issue #12271](https://github.com/ethereum/solidity/issues/12271)

`totalSupply` is modified only in the constructor. If we hide both `balanceOf`
and `totalSupply` with the private modifier, they should be modifiable only
inside the contract, thus inside the constructor and `transfer()` function. But
still the last assert cannot be proved.

