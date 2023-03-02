# deploy_trusted_state_flow.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/deployment/deploy_trusted_state_flow.sol)

Running:
```
solc deploy_trusted_state_flow.sol --model-checker-engine chc --model-checker-ext-calls=trusted --model-checker-show-unproved --model-checker-targets "assert,overflow"
```
We get:
```
Warning: CHC: Overflow (resulting value larger than 2**256 - 1) might happen here.
 --> smtCheckerNotes/deployment/deploy_trusted_state_flow/deploy_trusted_state_flo
w.sol:3:26:
  |
3 |     function inc() public { ++x; }
  |                             ^^^

Warning: CHC: Assertion violation happens here.
  --> smtCheckerNotes/deployment/deploy_trusted_state_flow/deploy_trusted_state_fl
ow.sol:14:3:
   |
14 |            assert(d.f() == 0); // should fail
   |            ^^^^^^^^^^^^^^^^^^
```
