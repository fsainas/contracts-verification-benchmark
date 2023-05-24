# Escrow 

## Specification
This contract allows a buyer to make a deposit and indicate a seller. The buyer
and seller can choose a payment address, and if choices match, the seller can
redeem the funds. If they do not match, the escrow system will arbitrate and
choose the correct address between the two. If the seller does not choose an
address, the buyer can redeem with a refund. The contract operates in five 
phases: Join, Choose, Redeem, Arbitrate, End $\{J,C,R,A,E\}$. Each phase has a set of callable functions.

## Versions
- **v1**: conformant to specification;
- **v2**: removed `require(fee_rate < 10000)` in the constructor.
- **v3**: contract is [ReentrancyGuard](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/ReentrancyGuard.sol)

## Properties
- **p1**: amount sent does not exceed deposit;
- **p2**: fee does not exceed deposit;
- **p3**: $p_c$ is the current phase and $p_p$ the previous one:
    1. $p_c = R \implies p_p = C$, if the current phase is redeem the previous one is Choose;
    1. $p_c = A \implies p_p = R$, if the current phase is arbitrate the previouse one is Redeem;
    1. $p_c = E \implies p_p = A \lor p_p = R \lor p_p = C$, if the current
       phase is End, the previous is Arbitrate, Redeem or Choose.
- **p4**: 
    1. The recipient of a payment from the contranct can only be `escrow`,
       `buyer_choice`, `seller_choice`, `buyer`.
    1. $\text{recipient} = \text{seller-choice} \implies \text{buyer-choice} = \text{seller-choice} \lor \text{escrow-choice} = \text{seller-choice}$
- **p5**: The `msg.sender` can only be `escrow`, `buyer` or `seller` for all
  functions except `redeem_arbitrated()`;
- **p6**: If `phase` is End and `escrow_choice` is not `address(0)` then
  `redeem_arbitrated()` has modified the balance of the contract.

## Experiments

|         | **p1**             | **p2**             | **p3**             | **p4**   | **p5**             | **p6** |
| ------- | ------------------ | ------------------ | ------------------ | -------- | ------------------ | ------ |
| **v1**  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x:[^1]  | :heavy_check_mark: | :x:    |
| **v2**  | :heavy_check_mark: | :question:         | :heavy_check_mark: | | |
| **v3**  |                    |                    |                    | :x:[^1]  | :heavy_check_mark: |

[^1]: "Uncaught exception"
