# Simple Transfer

## Specification
Simple Transfer is created with an initial balance, which consists of the
amount paid to the constructor plus the balance of the address of the contract
before deployment. There is a simple `withdraw()` function that transfers a
specified amount to the caller.

## Versions
- **v1**: 
    - `_deposited` variable keeps track of the total amount ever deposited, it
      never decrements.
    - `_sent` keeps track of the total amount sent by the contract, it never
      decrements.
- **v2**: instead of accessing `address(this).balance` directly, the `balance`
  variable is used to keep track of the balance. 

## Invariants
- **p1**: amount sent does not exceed deposit

## Experiments

|      | p1                 |
| ---- | ------------------ |
|**v1**| :x:                |
|**v2**| :heavy_check_mark: |
