# balance_receive_ext_calls
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/blockchain_state/balance_receive_ext_calls.sol)

External functions are intended to be called from outside the contract, and
sending Ether from an external function can introduce security risks. However,
an external function can receive Ether as part of the transaction that calls
it. Running `solc` with trusted external calls does not produce any warnings.

Running (CHC):
```
solc balance_receive_ext_calls.sol --model-checker-engine chc
```
We get:
```
Warning: CHC: Assertion violation happens here.
Counterexample:

_i = 0
x = 1143

Transaction trace:
C.constructor()
C.f(0)
    _i.ext() -- untrusted external call, synthesized as:
        C.f(0) -- reentrant call
            _i.ext() -- untrusted external call
 --> balance_receive_ext_calls.sol:9:3:
  |
9 |             assert(address(this).balance == x); // should fail
  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Running (BMC):
```
solc balance_receive_ext_calls.sol --model-checker-engine bmc
```
We get:
```
Warning: BMC: Assertion violation happens here.
 --> balance_receive_ext_calls.sol:9:3:
  |
9 |             assert(address(this).balance == x); // should fail
  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note: Counterexample:
  _i = 0
  address(this).balance = 39
  this = 7719
  x = 38

Note: Callstack:
Note: 
Note that external function calls are not inlined, even if the source code of the 
function is available. This is due to the possibility that the actual called contr
act has the same ABI but implements the function differently.

Warning: BMC: Assertion violation happens here.
  --> balance_receive_ext_calls.sol:10:3:
   |
10 |            assert(address(this).balance >= x); // should hold
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note: Counterexample:
  _i = 0
  address(this).balance = 0
  this = 1142
  x = 28101

Note: Callstack:
Note: 
Note that external function calls are not inlined, even if the source code of the 
function is available. This is due to the possibility that the actual called contr
act has the same ABI but implements the function differently.
```

The second assertion holds with CHC but not with BMC
