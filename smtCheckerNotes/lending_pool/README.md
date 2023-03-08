# Tests
This contracts are almost identical, except for the name of some variables. The
SMTchecker fails to prove some asserts with some name configurations.

The original code was written by
[Enrico Piseddu](https://github.com/enricopiseddu) and can be found
[here](https://github.com/enricopiseddu/lendingPool/blob/main/LendingPool.sol),
in the function `addReserve`.

## for_ok.sol
Running:
```
solc for_ok.sol --model-checker-engine chc --model-checker-show-unproved
```
We get no warnings, so the 2 asserts are proven true.

## for_arr_false_positive.sol
In this version `arr` becomes `res_arr` and `b` becomes `d`
Running:
```
solc for_arr_false_positive.sol --model-checker-engine chc --model-checker-show-unproved 
```
We get:
```
Warning: CHC: Assertion violation might happen here.
  --> for_arr_false_positive.sol:13:13:
   |
13 |             assert(n == res_arr.length);    // should hold
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
## for_arr_err.sol
In this version `arr` becomes `res_arr` and `b` becomes `reserveAlreadyExists`
(perhaps the significant property is the length).

Running:
```
solc for_arr_err.sol --model-checker-engine chc --model-checker-show-unproved
```
We get:
```
Warning: CHC: Error trying to invoke SMT solver.
  --> for_arr_err.sol:13:13:
   |
13 |             assert(n == res_arr.length);          // Error
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warning: CHC: Assertion violation might happen here.
  --> for_arr_err.sol:13:13:
   |
13 |             assert(n == res_arr.length);          // Error
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
