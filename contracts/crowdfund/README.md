# Crowdfund

## Specification

Crowdfund is contract a for conducting crowdfunding campaigns. It allows users
to donate ether to a specified receiver within a certain timeframe. The
contract ensures that the crowdfunding campaign is successful if the total
donated amount reaches a predefined goal. Otherwise, donors can reclaim their
donations after the donation period has ended.

## Properties

- **p1**: cannot withdraw if the contract balance is less than the goal.
- **p2**: if the contract balance is greater than or equal to the goal, then
  after the deposit phase the receiver can withdraw.
- **p3**: the contract balance cannot increase after the end of the deposit
  phase. This property should always be false, since a contract can receive ETH
  when its address is specified in a coinbase transaction or in a `selfdestruct`.
- **p4**: the only way to decrease the contract balance is by calling
  `withdraw()` or `reclaim()`.
- **p5**: if the goal amount is not reached and the deposit phase has ended, a donor can make a reclaim.
- **p6**: only a donor can make a reclaim.
- **p7**: if the goal amount is reached after the deposit period, only the receiver can withdraw from the contract
- **p8**: if the deposit period has ended, only `withdraw()` or `reclaim()` can be called.

## Versions

- **v1**: conformant to specification

## Experiments

### SolCMC

|        | p1  | p2  | p3  | p4  | p5  |
| ------ | --- | --- | --- | --- | --- |
| **v1** | TP  | N/D | TF  | N/D |
