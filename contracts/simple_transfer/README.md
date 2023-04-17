# Simple Transfer

## Specification
Simple Transfer is created with an initial balance which is the balance at
deployment time. Thus it is the sum of the balance of the address before the
deployment and what it was paid to the constructor.

The `deposited` variable keeps track of the total amount ever deposited to the
contract, it should never be decremented. Instead, the `sent` variable keeps
track of the total amount sent outside the contract and it should never be
incremented.

## Versions
- **v1**: conformant to specification;
- **v2**: instead of accessing `address(this).balance` directly, the `balance`
  variable is used to keep track of the balance. 

## Invariants
- **p1**: amount sent does not exceed deposit

## Experiments

|      | p1                 |
| ---- | ------------------ |
|**v1**| :x:                |
|**v2**| :heavy_check_mark: |
