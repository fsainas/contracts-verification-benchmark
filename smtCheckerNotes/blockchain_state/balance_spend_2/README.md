# balance_spend_2
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/blockchain_state/balance_spend_2.sol)

Running:
```
solc balance_spend_2.sol --model-checker-engine all
```
We get:

```
Warning: CHC: Assertion violation might happen here.
  --> balance_spend_2.sol:10:3:
   |
10 |            assert(address(this).balance > 0); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warning: CHC: Assertion violation happens here.
  --> balance_spend_2.sol:11:3:
   |
11 |            assert(address(this).balance > 80); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warning: CHC: Assertion violation happens here.
Counterexample:


Transaction trace:
C.constructor(){ msg.value: 101 }
C.f(0x12, 6)
C.f(0x0f, 9)
C.inv()
  --> balance_spend_2.sol:12:3:
   |
12 |            assert(address(this).balance > 90); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warning: BMC: Insufficient funds happens here.
 --> balance_spend_2.sol:7:3:
  |
7 |             _a.transfer(_v);
  |             ^^^^^^^^^^^^^^^
Note: Counterexample:
  _a = 0
  _v = 5

Note: Callstack:
Note:

Warning: BMC: Assertion violation happens here.
  --> balance_spend_2.sol:10:3:
   |
10 |            assert(address(this).balance > 0); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note: Counterexample:
  address(this).balance = 0
  this = 32278

Note: Callstack:
Note:
```
