# Solidity SMTChecker Analysis
This repository contains an analysis of the SMTChecker tool. SMTChecker is a
software verification tool that uses Satisfiability Modulo Theories (SMT)
solvers to check the correctness of Solidity smart contracts. It is integrated
into the Solidity compiler, making it a convenient and efficient option for
developers looking to ensure the reliability of their smart contracts. The
analysis in this repository aims to provide an overview of what the tool can
currently do and what it cannot. 

## Contracts
We have built a series of smart contracts to test the capabilities of SMTChecker:

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

## Experiments Legend
| Symbol | Meaning |
| ------ | ------- |
| TP | test passed as expected 
| TN | test failed as expected
| FP | test passed but should have failed (false positive)
| FN | test failed but should have passed (false negative)
| ? |  test does not seem to terminate
| N/D | property not definable
