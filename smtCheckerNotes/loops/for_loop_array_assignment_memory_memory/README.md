# for_loop_array_assignment_memory_memory.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/loops/for_loop_array_assignment_memory_memory.sol)

## Test 01
Running the test after uncommenting the asserts outside the loop produces 3
warnings related to the first one:
- Unused local variable: `uint[] memory a = b;`
- CHC: Out of bounds access happens here.
	- counter example: `n = 1`, `c = []`
	- The problem here is that if `n = 1` then `c` must have at least one
	  element for the second `require`.
- CHC: Assertion violation happens here: `assert(b[0] == c[0])`

Running:
```
solc test_01.sol --model-checker-engine chc --model-checker-timeout 0
```
We get:
```
Warning: Unused local variable.
 --> smtCheckerNotes/loops/for_loop_array_assignment_memory_memory/test_01.sol:7:3:
  |
7 |             uint[] memory a = b;
  |             ^^^^^^^^^^^^^^^

Warning: CHC: Out of bounds access happens here.
Counterexample:

n = 1
c = []

Transaction trace:
LoopFor2.constructor()
LoopFor2.testUnboundedForLoop(1, b, c)
  --> smtCheckerNotes/loops/for_loop_array_assignment_memory_memory/test_01.sol:15:18
:
   |
15 |            assert(b[0] == c[0]);
   |                           ^^^^

Warning: CHC: Assertion violation happens here.
Counterexample:

n = 1

Transaction trace:
LoopFor2.constructor()
LoopFor2.testUnboundedForLoop(1, b, c)
  --> smtCheckerNotes/loops/for_loop_array_assignment_memory_memory/test_01.sol:15:3:
   |
15 |            assert(b[0] == c[0]);
   |            ^^^^^^^^^^^^^^^^^^^^
```
