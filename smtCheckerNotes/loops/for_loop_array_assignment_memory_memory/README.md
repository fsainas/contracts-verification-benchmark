# for_loop_array_assignment_memory_memory.sol
Running the test after uncommenting only `assert(b[0] == c[0])` produces 3 warnings:
- Unused local variable: `uint[] memory a = b;`
- CHC: Out of bounds access happens here.
	- counter example: `n = 1`, `c = []`
	- The problem here is that if `n = 1` then `c` must have at least one
	  element for the second `require`.
- CHC: Assertion violation happens here: `assert(b[0] == c[0])`
