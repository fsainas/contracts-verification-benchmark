# Escrow Sent
These tests are aimed at verifying that the amount spent by the contract is always
less than or equal to the initial deposit. The functions are divided into
phases and have **chronological constraints** expressed using the block number.
SMTChecker does not assume that `block.number >= prev_block.number` (issue
[#10749](https://github.com/ethereum/solidity/issues/10749)), so we use the
technique shown [here](../../../smtCheckerNotes/block_number/). We use
`init_deposit` and `sent` as auxiliary variables, plus those needed for the
block number constraint.

## Escrow Basic Sent
This contract simulate sending funds using auxiliary variables and nothing more.
In addition, it assumes that all transfers are successful. \

How the state is modified:
```solidity
uint amount = deposit;
deposit -= amount;
sent += amount;
```

SMTChecker proves the invariant property in a short amount of time.

Command:
```
solc escrow_basic_sent_verified.sol --model-checker-engine chc --model-checker-timeout 0
```

Interestingly, changing the order of `t_id` and `prev_t_id` declarations has
a considerable impact on the speed.

## Escrow Sent with external calls
This test adds the actual `call()` method to transfer ether from the contract.
We also add a `require(success)` statement that reverts the transaction if
something goes wrong in the transfer.\
Despite the fact that the assert doesn't involve variables modified by the
`call()` method, SMTChecker does not seem to terminate after +4h.

Command:
```
solc escrow_sent_successful_call.sol \
--model-checker-engine chc \
--model-checker-timeout 0 \
--model-checker-targets "assert" \
--model-checker-show-unproved
```