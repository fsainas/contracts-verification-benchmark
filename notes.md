# Notes on SMTChecker tests
## Loops
### do_while_1_false_positives.sol
"false positives". The assert will be always true given the fact that the type
of `x` is uint.

### do_while_continue.sol
Probably beyond the purpose of the SMTChecker but there is no warning about the
infinite loop.

### for_1_fail.sol & for_1_false_positive.sol
You can reproduce the overflow warning only by removing `require(x < 100)` and
specifying the `--model-checker-targets "underflow,overflow"` option when running
`solc`.

### for_break_direct.sol
Produces the unreachable code warning on `++x`, but says nothing on the assert,
which can be false if `x != 0`.

### for_loop_6.sol
The assert will be always true because both 2 and 3 are less then 4. But the
value of `y` will be 2 when the assert is called.

### for_loop_array_assignment_memory_memory.sol
Running the test after uncommenting only `assert(b[0] == c[0])` produces 3 warnings:
- Unused local variable: `uint[] memory a = b;`
- CHC: Out of bounds access happens here.
	- counter example: `n = 1`, `c = []`
	- The problem here is that if `n = 1` then `c` must have at least one
	  element for the second `require`.
- CHC: Assertion violation happens here: `assert(b[0] == c[0])`

## Deployment
### deploy_trusted.sol
"By default, the SMTChecker does not assume that compile-time available code is
the same as the runtime code for external calls" from the documentation.
`--model-checker-ext-calls=trusted` option must be set.
