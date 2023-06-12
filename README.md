# An open benchmark for evaluation of smart contracts verification tools

We introduce an open benchmark of smart contracts and relevant security properties
to be used for the evaluation and comparison of verification tools.

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
- [Tiny AMM](contracts/tinyamm/)
- [Payment Splitter](contracts/payment_splitter/)
- [Social Recovery Wallet](contracts/social_recovery_wallet/)

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
| ?      | Timeout                                                        |
| N/D    | property not definable with the tool                           |

We test our benchmark with two mainstream verification tools:
[SolCMC](https://verify.inf.usi.ch/publications/2022/solcmc-solidity-compiler%E2%80%99s-model-checker) and [Certora](https://www.certora.com/).
