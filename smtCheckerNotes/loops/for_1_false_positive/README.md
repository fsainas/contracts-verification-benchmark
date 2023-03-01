# for_1_false_positive.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/for_1_false_positive.sol)

You can reproduce the overflow warning only by removing `require(x < 100)` and
specifying the `--model-checker-targets "underflow,overflow"` option when running
`solc`.

## Test 01
Running:
```
solc test_01.sol --model-checker-engine chc --model-checker-targets "underflow,overflow,assert" --model-checker-timeout 0
```
We get:
```
Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here.
Counterexample:

x = 11579208923731619542357098500868790785326998466564056403945758400791312963993
5
i = 0

Transaction trace:
C.constructor()
C.f(11579208923731619542357098500868790785326998466564056403945758400791312963993
5)
 --> smtCheckerNotes/loops/for_1_false_positive/test_01.sol:5:8:
  |
5 |                     x = x + 1;
  |                         ^^^^^
```
