# deploy_trusted.sol
[Original](https://github.com/ethereum/solidity/blob/develop/test/libsolidity/smtCheckerTests/deployment/deploy_trusted.sol)

"By default, the SMTChecker does not assume that compile-time available code is
the same as the runtime code for external calls" from the documentation.
`--model-checker-ext-calls=trusted` option must be set.
