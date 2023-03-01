# do_while_1_false_positives.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/do_while_1_false_positives.sol)

"false positives". The assert will be always true given the fact that the type
of `x` is uint and if `x == 0`, `x` will be incremented at least once anyway.

## test 01
If we remove `require(x < 100);` there is a risk of overflow.
Running: 
```
solc test_01.sol --model-checker-engine chc --model-checker-targets "underflow,overflow"
```
We get:
```
Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here.
Counterexample:

x = 115792089237316195423570985008687907853269984665640564039457584007913129639935

Transaction trace:
C.constructor()
C.f(115792089237316195423570985008687907853269984665640564039457584007913129639935
)
 --> smtCheckerNotes/loops/do_while_1_false_positives/test_01.sol:5:8:
  |
5 |                     x = x + 1;
  |                         ^^^^^
```
