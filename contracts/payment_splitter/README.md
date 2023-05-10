# Payment Splitter
[Original contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/finance/PaymentSplitter.sol) by OpenZeppelin.

## Specification
This contract allows to split Ether payments among a group of accounts. The
sender does not need to be aware that the Ether will be split in this way,
since it is handled transparently by the contract.
 
The split can be in equal parts or in any other arbitrary proportion. The way
this is specified is by assigning each account to a number of shares. Of all
the Ether that this contract receives, each account will then be able to
claim an amount proportional to the percentage of total shares they were
assigned. The distribution of shares is set at the time of contract
deployment and can't be updated thereafter.

`PaymentSplitter` follows a _pull payment_ model. This means that payments
are not automatically forwarded to the accounts but kept in this contract,
and the actual transfer is triggered as a separate step by calling the
`release()` function. 

## Versions
- **v1**: conformant to specification.

## Invariants
- **inv1**: every account in `payees` is a non-zero address.
- **inv2**: if the first account in `payees` is `address(0x1)` then
  `shares[address(0x1)]` $\neq 0$ 
- **inv3**: if the first account in `payees` is `address(0x1)` then 
  `shares[address(0x1)]` $= 0$ (should fail)

## Experiments

|        | **inv1**   | **inv2**   | **inv3**           |
| ------ | ---------- | ---------- | ------------------ |
| **v1** | :question: | :question: | :heavy_check_mark: |
