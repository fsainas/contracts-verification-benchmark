# Solidity SMTChecker Analysis
This repository contains an analysis of the SMTChecker tool. SMTChecker is a
software verification tool that uses Satisfiability Modulo Theories (SMT)
solvers to check the correctness of Solidity smart contracts. It is integrated
into the Solidity compiler, making it a convenient and efficient option for
developers looking to ensure the reliability of their smart contracts. The
analysis in this repository aims to provide an overview of what the tool can
currently do and what it cannot. 

## Contracts
We've built a series of smart contracts to test the capabilities of SMTChecker:

- [Escrow](contracts/escrow/)

## More tests
We've also created some tests similar to those in the 
[soldity repo](https://github.com/ethereum/solidity/tree/develop/test/libsolidity/smtCheckerTests).
