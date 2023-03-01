# for_1_fail.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/for_1_fail.sol)

Can reproduce the overflow warning only by removing `require(x < 100)` and
specifying the `--model-checker-targets "underflow,overflow"` option when running
`solc`.

## test 01
Running:
```
solc test_01.sol --model-checker-engine chc --model-checker-targets "underflow,
overflow,assert"
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
 --> smtCheckerNotes/loops/for_1_fail/test_01.sol:6:8:
  |
6 |                     x = x + 1;
  |                         ^^^^^

Warning: CHC: Assertion violation happens here.
Counterexample:

x = 14

Transaction trace:
C.constructor()
C.f(4)
 --> smtCheckerNotes/loops/for_1_fail/test_01.sol:8:3:
  |
8 |             assert(x < 14);
  |             ^^^^^^^^^^^^^^
```
