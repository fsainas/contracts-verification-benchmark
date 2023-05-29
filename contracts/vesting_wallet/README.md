# Vesting Wallet

Original contract by [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/finance/VestingWallet.sol)

## Specification

Vesting Wallet handles the vesting of ethers for a given beneficiary. The
vesting follows a given vesting schedule, the default is a linear curve. Every
ether transferred to this contract will follow the vesting schedule as if it
was locked from the beginning. Consequently, if the vesting has already
started, any amount sent to this contract will be immediately releasable.

## Versions

- **v1**: conformant to specification;

## Properties

- **p1**: the amount releasable is always less than or equal to the contract
  balance
- **p2**: if `block.timestamp > duration + start` then `releasable() ==
  address(this).balance`
- **p3**: if `releasable()` is called at two different timestamps before the
  end of the vesting and the balance of the contract has not changed, then the
  the value returned by the first call is less than the second.

## Experiments

|      | p1                 | p2                    | p3         |
| ---- | ------------------ | --------------------- | ---------- | 
|**v1**| :x:                | :question:            | :question: |
