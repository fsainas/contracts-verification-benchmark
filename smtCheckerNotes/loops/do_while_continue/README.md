# do_while_continue.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/do_while_continue.sol)

Probably beyond the purpose of the SMTChecker but there is no warning about the
infinite loop.

Running:
```
solc do_while_continue.sol --model-checker-engine chc
```
We get:
```
Warning: Unreachable code.
 --> smtCheckerNotes/loops/do_while_continue/do_while_continue.sol:6:4:
  |
6 |                     x = 1;
  |                     ^^^^^
```
