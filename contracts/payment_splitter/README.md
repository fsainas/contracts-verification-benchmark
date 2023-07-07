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
- **v1**: conformant to specification

## Invariants
- **p1**: for all accounts `a` in `payees`, `a != address(0)`
- **p2**: if `payees[0] == addr` then `shares[addr] == 0` (should fail)
- **p3**: for all addresses `addr` in `payees`, `shares[a] > 0`
- **p4**: for all addresses `addr` in `payees`, `releasable(a) <= address(this).balance`
- **p5**: the sum of the releasable funds for every accounts is equal to
  `address(this).balance`

## Experiments

### SolCMC

|        | p1  | p2  | p3  | p4  | p5  |
| ------ | --- | --- | --- | --- | --- |
| **v1** | ?   | TN  | ?   | FN  | FN  |

### Certora

|        | p1  | p2  | p3  | p4  | p5  |
| ------ | --- | --- | --- | --- | --- |
| **v1** | FN  | FN  | TN  | FN  |
