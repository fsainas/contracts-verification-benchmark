# Escrow 

## Specification
This contract allows a buyer to make a deposit and indicate a seller. The buyer
and seller can choose a payment address, and if choices match, the seller can
redeem the funds. If they do not match, the escrow system will arbitrate and
choose the correct address between the two. If the seller does not choose an
address, the buyer can redeem with a refund. The contract operates in three
phases: Join, Choose, and Redeem. Each phase has a set of callable functions.

## Versions
- **v1**: conformant to specification.

## Invariants
- **inv1**: amount sent does not exceed deposit.

## Experiments

|      | **inv1**           |
| ---- | ------------------ |
|**v1**| :heavy_check_mark: |
