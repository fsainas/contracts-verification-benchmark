# for_break_direct.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/for_break_direct.sol)

Produces the unreachable code warning on `++x`, but says nothing on the assert
which can be false if `x != 0`.

Running:
```
solc for_break_direct.sol --model-checker-engine chc --model-checker-targets "assert" --model-checker-timeout 0
```
We get:
```
Warning: Unreachable code.
 --> smtCheckerNotes/loops/for_break_direct/for_break_direct.sol:3:23:
  |
3 |             for (x = 0; x < 10; ++x)
  |                                 ^^^
```
