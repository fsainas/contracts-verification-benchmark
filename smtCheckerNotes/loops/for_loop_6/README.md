# for_loop_6.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/for_loop_6.sol)

The assert will be always true because both 2 and 3 are less then 4. But the
value of `y` will be 2 when the assert is called.

## test 01
In this test we check if `y` will be always equal to 2 after the loop.
There are no warnings after running:
```
solc test_01.sol --model-checker-engine chc --model-checker-timeout 0 --model-checker-targets "assert"
```
