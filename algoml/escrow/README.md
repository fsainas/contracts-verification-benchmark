# Escrow 

## Bug or vulnerabilities found thanks to SMTChecker
- Fee greater than deposit (underflow warning)

## feeRate bug
In the original algoml contract there is probably a bug where the fee for the
escrow can be more than the deposit.

## Escrow_sent.sol
SMTChecker cannot prove that the amount sent by the contract is always equal or less than the initial amount deposited.

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
changes he's choice. Therefore the assert is false

### Steps to reproduce
```
solc Escrow_less_safe_eChoice.sol --model-checker-engine chc --model-checker-timeout 0 --model-checker-show-unproved
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

## Escrow_block_number_implication.sol
Same `block.number` problem here.
If we try to prove that:\
$\texttt{block.number} < \texttt{end\_redeem} \implies \texttt{eChoice} \neq
\texttt{address(0)}$\
By running `solc` with the same options the output is:
```
Warning: CHC: Assertion violation happens here.
Counterexample:
end_join = 7720, end_choice = 7721, end_redeem = 7722, fee_rate = 10000, buyer = 0x0, 
seller = 0x0 , escrow = 0x0, deposit = 0, buyer_choice = 0x0, seller_choice = 0x01, 
eChoice = 0x01

Transaction trace:
Escrow.constructor(0x0, 7720, 7721, 7722, 10000){ block.number: 7719 }
State: end_join = 7720, end_choice = 7721, end_redeem = 7722, fee_rate = 10000,
buyer = 0x0, seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0,
seller_choice = 0x0, eChoice = 0x0

Escrow.choose(0x01){ msg.sender: 0x0 }
State: end_join = 7720, end_choice = 7721, end_redeem = 7722, fee_rate = 10000,
buyer = 0x0, seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0,
seller_choice = 0x01, eChoice = 0x0

Escrow.arbitrate(0x01){ block.number: 7723, msg.sender: 0x0 }
    escrow.call{value: fee}("") -- untrusted external call
State: end_join = 7720, end_choice = 7721, end_redeem = 7722, fee_rate = 10000,
buyer = 0x0, seller = 0x0, escrow = 0x0, deposit = 0, buyer_choice = 0x0,
seller_choice = 0x01, eChoice = 0x01

Escrow.redeem(){ block.number: 7721 }
    buyer.call{value: deposit}("") -- untrusted external call, synthesized as:
        Escrow.invariant(){ block.number: 7721 } -- reentrant call

   --> Escrow_block_number_implication.sol:137:9:
    |
137 |         assert(!(block.number < end_redeem && !(eChoice == address(0))));
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
The block number of `arbitrate()` is greater than the one of `redeem()` which
is executed after.

## Escrow_underflow_overflow.sol
SMTChecker easily proves that no underflow can happen.
It has more difficulty in proving that there are no overflows, indeed it does not seem to terminate.

## Notes
- SMTChecker assumes that `address(0)` can do transactions. Sometimes it can be
  helpful to add the constraint explicitly.