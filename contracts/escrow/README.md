# Escrow 

## Specification
This contract allows a buyer to make a deposit and indicate a seller. The buyer
and seller can choose a payment address, and if choices match, the seller can
redeem the funds. If they do not match, the escrow system will arbitrate and
choose the correct address between the two. If the seller does not choose an
address, the buyer can redeem with a refund. The contract operates in three
phases: Join, Choose, and Redeem. Each phase has a set of callable functions.

## Versions
- **v1**: conformant to specification;
- **v2**: non reentrant functions with
  [ReentrancyGuard](lib/ReentrancyGuard.sol).
    - **v2.1**: no `require(fee_rate <= 10000)` in the constructor.

## Invariants
- **inv1**: amount sent does not exceed deposit.
- **inv2**: fee does not exceed deposit.

## Experiments

|         | **inv1**           | **inv2**               |
| ------- | ------------------ | ---------------------- |
|**v1**   | :question:         | :question:             |
|**v2**   | :heavy_check_mark: | :heavy_check_mark:     |
|**v2.1** | :heavy_check_mark: | :heavy_check_mark:[^1] |

[^1]: To be investigated.
