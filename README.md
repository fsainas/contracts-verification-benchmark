# An open benchmark for evaluating smart contracts verification tools

This is an open project to construct a benchmark of Solidity smart contracts
for evaluating and comparing verification tools.

The repo contains a set of use cases: each use case is associated with
a set of Solidity implementations (possibly, containing bugs), 
and a set of properties against which to assess verification tools.
Here we are also interested in properties that go beyond the capabilities
of the current tools, hoping that they can be of inspiration for 
more precise verification techniques.

## Contracts

The benchmark currently comprises several versions (correct or bugged) of the following use cases:
- [Simple Transfer](contracts/simple_transfer/)
- [Token Transfer](contracts/token_transfer/)
- [Bank](contracts/bank/)
- [Lottery](contracts/lottery/)
- [Escrow](contracts/escrow/)
- [Vesting Wallet](contracts/vesting_wallet/)
- [Vault](contracts/vault/)
- [Crowdfund](contracts/crowdfund/)
- [Hash Timed Locked Contract](contracts/htlc/)
- [Constant-product AMM](contracts/tinyamm/)
- [Payment Splitter](contracts/payment_splitter/)
- [Social Recovery Wallet](contracts/social_recovery_wallet/)


## Verification tools

Currently the benchmark supports the following verification tools:
- [SolCMC](https://verify.inf.usi.ch/publications/2022/solcmc-solidity-compiler%E2%80%99s-model-checker)
- [Certora](https://www.certora.com/)

## Evaluating a verification tool

For each use case, we evaluate the performance of a verification tool
as a matrix, where columns represent different contract properties, and
rows represent different implementations of the use case.
For each entry of the matrix, we summarize the output of the tool as follows:

| Symbol | Meaning                                                        |
| ------ | -------                                                        |
| TP     | True Positive  (property holds, verification succeeds)         |
| TN     | True Negative  (property does not hold, verification fails)    |
| FP     | False Positive (property does not hold, verification succeeds) |
| FN     | False Negative (property holds, verification fails)            |
| ND     | Property not definable with the tool                           |

Additionally, we mark with ! the classifications TP,TN,FP,FN, when the verification tool 
guarantees the correctness of the output. 
Following our [methodological notes](methodology/), we map the outputs of the 
verification tools according to the following table:

| Suffix  | SolCMC output           | Certora ouput  |
|---------|-------------------------|----------------|
| P       |                         | Satisfy green  |
| P!      | Property is valid       | Assert green   |
| N       | Property might be false | Assert red     |
| N       | Timeout                 | Timeout        |
| N!      | Property is false       | Satisfy red    | 

## Extending the benchmark

Each use case directory includes:
- `skeleton.json`
- `ground-truth.csv`
- `versions` directory
- `Makefile`
- A directory for every verification tool used

### skeleton.json

This file stores the use case's **name**, **specification** and **properties**
defined in natural language:
```
{
    "name": "Simple Transfer",
    "specification": "The contract has an initial balance...",
    "properties": [
        "the overall sent amount does not exceed the initial deposit.",
        ... 
    ]
}
```

### ground-truth.csv

This file defines the ground truth for the corresponding use case. Lines of the
csv have the form:
```
property,version,sat
```
where `sat` is 1 when the property holds on the given version, and 0 when it
does not hold. The ground truth is constructed manually, and (in some cases)
confirmed by the verification tools.

### Versions Directory

The `versions/` directory contains various Solidity variants of the use case
contract, with version definitions in natural language written using the
NatSpec format and the `@custom:version` tag:
```
/// @custom:version reentrant `withdraw`.
```

### Makefile

The Makefile defines three commands:
1. `make plain`: This command generates the README without experiment results. It
   utilizes `skeleton.json`, `ground-truth.csv` and version files from
   `versions/`.
1. `make verif`: This command calls the Makefiles of verification tools and runs experiments.
1. `make all`: This command runs experiments generates the complete README.
