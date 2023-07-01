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
- [Lottery](contracts/Lottery/)
- [Escrow](contracts/escrow/)
- [Vesting Wallet](contracts/vesting_wallet/)
- [Vault](contracts/vault/)
- [Crowdfund](contracts/crowdfund/)
- [Hash Timed Locked Contract](contracts/htlc/)
- [Constant-product AMM](contracts/tinyamm/)
- [Payment Splitter](contracts/payment_splitter/)
- [Social Recovery Wallet](contracts/social_recovery_wallet/)

## Using the benchmark

Each use case folder includes a file `in.csv` that defines the ground truth for that use case.
Lines of the csv have the form:
```
property,version,sat
```
where `sat` is 1 when the property holds on the given version, and 0 when it does not hold.
The ground truth is constructed manually, and (in some cases) confirmed by the verification tools.

The `contracts` folder contains a Python script to automatize the execution of verification tools.
For instance, to run SolCMC on the `simple_transfer` use case, execute the command:
```
python run.py -d simple_transfer -t solcmc
```
The output is written in the file `simple_transfer/solcmc/out.csv`.

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
| ?      | Timeout / Unknown                                              |
| N/D    | Property not definable with the tool                           |

