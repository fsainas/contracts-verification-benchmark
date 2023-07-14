# Escrow 

## Specification

This contract allows a buyer to make a deposit and indicate a seller. The buyer
and seller can choose a payment address, and if choices match, the seller can
redeem the funds. If they do not match, the escrow system will arbitrate and
choose the correct address between the two. If the seller does not choose an
address, the buyer can redeem with a refund. The contract operates in five 
phases: Join, Choose, Redeem, Arbitrate, End $\{J,C,R,A,E\}$. Each phase has a set of callable functions.

## Properties

- **p1**: fee does not exceed deposit
- **p2**: if the current phase is Redeem the previous one is Choose
- **p3**: if the current phase is Arbitrate the previouse one is Redeem
- **p4**: if the current phase is End, the previous one is Arbitrate, Redeem or
  Choose.
- **p5**: If `phase` is End and `escrow_choice` is not `address(0)` then
  `redeem_arbitrated()` has modified the balance of the contract.
- **p6**: The `msg.sender` can only be `escrow`, `buyer` or `seller` for all
  functions except `redeem_arbitrated()`;

## Versions

- **v1**: conformant to specification;
- **v2**: removed `require(fee_rate < 10000)` from the constructor.
- **v3**: contract is [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/ReentrancyGuard.sol)


## Experiments

### SolCMC

|         | p1  | p2  | p3  | p4  | p5  | p6  |
| ------- | --- | --- | --- | --- | --- | --- |
| **v1**  | TP  | TP  | TP  | TP  | TP  | TP  |
| **v2**  | TP  | TP  | TP  | TP  | TP  | TP  |
| **v3**  | TP  |

### Certora

|         | p1  | p2  | p3  | p4  | p5  | p6  |
| ------- | --- | --- | --- | --- | --- | --- |
| **v1**  |     | TP  | TP  | TP  | FN  | TP  |
| **v2**  | 
| **v3**  | 
