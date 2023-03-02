# constructor_hierarchy_3
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/functions/constructor_hierarchy_3.sol)

Contract A inherits from contract B, and contract B inherits from contract C.
The constructor of contract C will be called first, followed by the constructor
of contract B, and finally the constructor of contract A will be called.
Therefore the second `assert` will always be false, even if it were 
`assert(a == x + 2)`.

Running:
```
solc constructor_hierarchy_3.sol --model-checker-engine chc --model-checker-ext-calls=trusted --model-checker-show-unproved --model-checker-targets "assert,overflow"
```
We get:
```
Warning: CHC: Overflow (resulting value larger than 2**256 - 1) happens here.
Counterexample:
a = 0
x = 115792089237316195423570985008687907853269984665

Transaction trace:
A.constructor(11579208923731619542357098500868790785
3129639934)
  --> smtCheckerNotes/functions/constructor_hierarch
l:15:29:
   |
15 |    constructor(uint x) B(x) C(x + 2) {
   |                               ^^^^^

Warning: CHC: Assertion violation happens here.
Counterexample:
a = 0
x = 0

Transaction trace:
A.constructor(0)
  --> smtCheckerNotes/functions/constructor_hierarch
l:17:3:
   |
17 |            assert(a == x + 2);
   |            ^^^^^^^^^^^^^^^^^^
```
