# Escrow Sent
These tests are aimed at verifying that the amount spent by the contract is
always less than or equal to the initial deposit. To do this we use the assert
`assert(sent <= init_deposit)`inside the `invariant()` function. The functions
are divided into phases and have **chronological constraints** expressed using
the block number. SMTChecker does not assume that `block.number >=
prev_block.number` (issue
[#10749](https://github.com/ethereum/solidity/issues/10749)), so we use the
technique shown [here](../../../smtCheckerNotes/block_number/). 

Ghost variables:
- `uint init_deposit` $\to$ initial deposit;
- `uint sent` $\to$ amount sent by the contract;
- [block number](../../../smtCheckerNotes/block_number/) related variables.

## Escrow Sent No External Calls :heavy_check_mark:
This contract simulate sending funds using ghost variables and nothing more.
In addition, it assumes that all transfers are successful.

How the state is modified:
```solidity
sent += deposit;
deposit = 0;
```

SMTChecker proves the invariant property in a short amount of time.

Command:
```
solc escrow_basic_sent_verified.sol --model-checker-engine chc --model-checker-timeout 0
```

Interestingly, changing the order of `t_id` and `prev_t_id` declarations has
a considerable impact on the speed.

## Escrow Sent with External Calls :x:
This test adds the actual `call()` primitive to transfer ether from the contract.
We also add a `require(success)` statement that reverts the transaction if
something goes wrong in the transfer:
```solidity
(bool success,) = recipient.call{value: sent}("");
require(success);
```
Despite the fact that the assert doesn't involve variables modified by the
`call()` method, SMTChecker does not seem to terminate after +4h.

Command:
```
solc escrow_sent_external_calls.sol \
--model-checker-engine chc \
--model-checker-timeout 0 \
--model-checker-targets "assert" \
--model-checker-show-unproved
```

## Escrow Sent with Failure :x:
We simulate the possibility of transaction failure by using an expression that
can be equal to 1 or 0:

```solidity
uint amount = deposit;
deposit -= amount;
sent += amount; 

uint success = block.timestamp % 2;
if (success == 0) {
    deposit += amount;
    sent -= amount;
}
```
Even in this case it does not terminate.

## Escrow Sent with Revert :heavy_check_mark:
In this test we use `revert()` to restore the state in case of failure, rather
than manually writing to storage.
```solidity
uint success = block.timestamp % 2;
if (success == 0) revert();
```
SMTChecker proves `assert(sent <= init_deposit)` in ~3.60s.
