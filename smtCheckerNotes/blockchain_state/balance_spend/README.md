### balance_spend
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/blockchain_state/balance_spend.sol)

Running (CHC):
```
solc balance_spend.sol --model-checker-engine chc --model-checker-timeout 0 
```
We get:
```
Warning: CHC: Assertion violation happens here.
Counterexample:
c = 2

Transaction trace:
C.constructor(){ msg.value: 104 }
State: c = 0
C.f(0x14, 9)
State: c = 1
C.f(0x10, 9)
State: c = 2
C.inv()
  --> balance_spend.sol:14:3:
   |
14 |            assert(address(this).balance > 90); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Running (CHC):
```
solc balance_spend.sol --model-checker-engine bmc --model-checker-timeout 0 
```
We get:
```
Warning: BMC: Insufficient funds happens here.
  --> balance_spend.sol:10:3:
   |
10 |            _a.transfer(_v);
   |            ^^^^^^^^^^^^^^^
Note: Counterexample:
  _a = 0
  _v = 0
  c = 1

Note: Callstack:
Note:

Warning: BMC: Assertion violation happens here.
  --> balance_spend.sol:13:3:
   |
13 |            assert(address(this).balance > 80); // should hold
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note: Counterexample:
  address(this).balance = 62
  c = 0
  this = 31111

Note: Callstack:
Note:

Warning: BMC: Assertion violation happens here.
  --> balance_spend.sol:14:3:
   |
14 |            assert(address(this).balance > 90); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note: Counterexample:
  address(this).balance = 0
  c = 0
  this = 7176

Note: Callstack:
Note:
```
BMC gives us the insufficient funds warning.
The first assert should hold because the function f can transfer funds only
twice and for a maximum value of 9. Thus the maximum value that the contract
can transfer is 18. 

## Test 01
If we change the first assert to `assert(address(this).balance >= 82)` it holds
anyway.

Running (CHC - BMC):
```
solc test_01.sol --model-checker-engine all 
```
We get:
```
Warning: CHC: Assertion violation happens here.
Counterexample:
c = 2

Transaction trace:
C.constructor(){ msg.value: 101 }
State: c = 0
C.f(0x15de, 8)
State: c = 1
C.f(0xffffffffffffffffffffffffffffffffffffe87d, 9)
State: c = 2
C.inv()
  --> test_01.sol:14:3:
   |
14 |            assert(address(this).balance > 90); // should fail
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warning: BMC: Insufficient funds happens here.
  --> test_01.sol:10:3:
   |
10 |            _a.transfer(_v);
   |            ^^^^^^^^^^^^^^^
Note: Counterexample:
  _a = 0
  _v = 0
  c = 1

Note: Callstack:
Note:
```
