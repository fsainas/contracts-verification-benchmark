# Escrow 

## feeRate bug
In the original algoml contract there is probably a bug where the fee for the
escrow can be more than the deposit.

## Escrow_sent.sol
When trying to prove `assert(sent <= deposit)` in the `invariant()` function it
seems that SMTChecker does not terminate.

## Escrow_safe_eChoice.sol
SMTChecker successfully proved that `eChoice` is always `address(0)`, when the
`arbitracte()` function is not yet called, or equal to `buyer_choice` or
`seller_choice`.

Time: 39.10s

## Escrow_less_safe_eChoice.sol
If we remove the requires in the `choose()` function, the buyer and the seller
can change their choice as many times they want. SMTChecker finds a
counterexample: the escrow calls the the `arbitrate()` function and agrees with
the seller choice, then the seller calls again the `choose()` function and
changes he's choice. The assert is therefore false.

### Steps to reproduce
```
time solc Escrow_less_safe_eChoice.sol --model-checker-engine chc --model-checker-timeout 0 --model-checker-show-unproved
```
Output:
```
Warning: CHC: Assertion violation happens here.
Counterexample:
end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x01,
seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0, seller_choice = 0x0, 
eChoice = 0x01, last_choose_block = 0, last_arbitrate_block = 4

Transaction trace:
Escrow.constructor(0x0, 1, 2, 3, 10000){ block.number: 0 }
State: end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x0, 
seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0, seller_choice = 0x0, 
eChoice = 0x0, last_choose_block = 0, last_arbitrate_block = 0
Escrow.join(0x0){ msg.sender: 0x01, msg.value: 1 }
State: end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x01, 
seller = 0x0, escrow = 0x0, deposit = 1, buyer_choice = 0x0,
seller_choice = 0x0, eChoice = 0x0, last_choose_block = 0, last_arbitrate_block = 0
Escrow.choose(0x01){ block.number: 0, msg.sender: 0x0 }
State: end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x01, 
seller = 0x0, escrow = 0x0, deposit = 1, buyer_choice = 0x0,
seller_choice = 0x01, eChoice = 0x0, last_choose_block = 0,
last_arbitrate_block = 0
Escrow.arbitrate(0x01){ block.number: 4, msg.sender: 0x0 }
    escrow.call{value: fee}("") -- untrusted external call
State: end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x01, 
seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0,
seller_choice = 0x01, eChoice = 0x01, last_choose_ block = 0,last_arbitrate_block = 4
Escrow.choose(0x0){ block.number: 0, msg.sender: 0x0 }
State: end_join = 1, end_choice = 2, end_redeem = 3, fee_rate = 10000, buyer = 0x01, 
seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0, seller_choice = 0x0, 
eChoice = 0x01, last_choose_b lock = 0, last_arbitrate_block = 4
Escrow.invariant()
   --> algoml/Escrow_less_safe_eChoice.sol:154:9:
    |
154 |         assert(eChoice == address(0) || eChoice == buyer_choice || eChoice == seller_choice);
    |
```

But there is a problem. In the transaction trace the `choose()` function is
called after the `arbitrate()` function, which is impossible because `choose()`
is guaranteed to be called before the `end_choice` block by the
`beforeEndChoice` modifier, which must be less than `end_redeem` block for the
constraints in the constructor, and `arbitrate()` can be called only after the
`end_redeem` block because of the `afterEndReedem` modifier. SMTChecker does
not assume that the block number of a subsequent transaction is greater than or
equal to the previous one. [#10749](https://github.com/ethereum/solidity/issues/10749)

## 
