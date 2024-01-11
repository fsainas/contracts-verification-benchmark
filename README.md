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

> We are currently updating the contracts to the standard described in the "[extending the benchmark](#extending-the-benchmark)" section. Up-to-date contracts are marked with :white_check_mark:.

The benchmark currently comprises several versions (correct or bugged) of the following use cases:
- [Zero-token Bet](contracts/zerotoken_bet/) :white_check_mark:
- [Zero-token Bank](contracts/zerotoken_bank/) :white_check_mark:
- [Simple Transfer](contracts/simple_transfer/) :white_check_mark:
- [Token Transfer](contracts/token_transfer/) :white_check_mark:
- [Call Wrapper](contracts/call-wrapper/) :white_check_mark:
- [Bank](contracts/bank/) :white_check_mark:
- [Lottery](contracts/lottery/)
- [Escrow](contracts/escrow/)
- [Vesting Wallet](contracts/vesting_wallet/) :white_check_mark:
- [Vault](contracts/vault/) :white_check_mark:
- [Crowdfund](contracts/crowdfund/) :white_check_mark:
- [Hash Timed Locked Contract](contracts/htlc/) :white_check_mark:
- [Constant-product AMM](contracts/tinyamm/) :white_check_mark:
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

| Suffix  | SolCMC output           | Certora output |
|---------|-------------------------|----------------|
| P       |                         | Satisfy green  |
| P!      | Property is valid       | Assert green   |
| N       | Property might be false | Assert red     |
| N       | Timeout                 | Timeout        |
| N!      | Property is false       | Satisfy red    | 

## Extending the benchmark

In the `contracts/` directory, run the following command to initialize a new use case:

```
$ make init name=<usecase-name>
```
This command creates a new directory and provides the template to start your work.

### Use case directory structure

Each use case directory must include the following files:
- `skeleton.json`
- `ground-truth.csv`
- `versions` directory
- `Makefile`
- A directory for every verification tool used

Find a minimal example in [`contracts/template/`](contracts/template) directory.

#### skeleton.json

This file stores the use case's **name**, **specification** and **properties**
defined in natural language:
```
{
    "name": "Simple Transfer",
    "specification": "The contract has an initial balance...",
    "properties": {
        "sent_a": "the overall sent amount does not exceed the initial deposit.",
        ... 
    }
}
```
You can store specifications in a separate file, use the following syntax to
indicate the path:

```
"specification": "file:<relative_path>",
```
Here, the file path is relative to the path of the use case (e.g.
`simple_transfer/spec.md` would be `file:spec.md`).

#### ground-truth.csv

This file defines the ground truth for the corresponding use case. Lines of the
csv have the form:
```
property,version,sat,footnote
```
where `sat` is 1 when the property holds on the given version, and 0 when it
does not hold. The ground truth is established manually and, in some cases,
confirmed by the verification tools. Furthermore, there is the option to append
footnotes, which will be displayed in the readme file of the use case.

#### Versions Directory

The `versions/` directory contains various Solidity variants of the use case
contract, with version definitions in natural language written using the
NatSpec format and the `@custom:version` tag:
```
/// @custom:version reentrant `withdraw`.
```

#### Makefile

The Makefile defines the following commands:
1. `make plain`: generates the README without experiment results. It utilizes `skeleton.json`, `ground-truth.csv` and version files from `versions/`.
1. `make solcmc`: run the SolCMC experiments. By default, the timeout is set to 10 minutes. Use `make solcmc to=<int>` to set a different timeout for each query in seconds.
1. `make certora`: runs the Certora experiments; results are written in the README.
1. `make all`: runs experiments with all verification tools and generates the complete README.
1. `make clean`: removes build directories from verification tool directories.
1. `make cleanr`: removes the readme file.


### SolCMC directory structure

SolCMC directories contain:

- `Makefile`: to run solcmc experiments and manage contracts building.
- Property files.

An example of a property file:

```
function p(<T> y, ...) public {
    // preconditions
    require(x != y);
    // ...

    // some change in state
    f1(x, y);
    f2();
    // ...

    // postconditions
    assert(x != y);
    // ...
}
```

In this case `x` could be a state variable of the contract and `y` an arbitrary value of type `T`.

### Certora directory structure

Certora directories contain:
- `Makefile`: to run certora experiments and manage contracts building.
- `getters.sol`: a collection of getters for contract state variables, useful to write certora specifications.
- `methods.spec`: methods declaration to use in certora specifications.
- Specification files.

An example of a specification file:

```
rule P1 {
    env e;

    mathint y;
    x = getX();
    require x != y;

    f1(x,y);
    f2();

    assert x != y;
}
```

### Version specifc properties

Property files must follow the specified naming conventions:

- For general properties, the file should be named as `p<property_number>.sol`.
- If the property is associated with a specific contract version, use the
  format `p<property_number>_v<version_number>.sol`.

The tool manages the matching of properties and versions. It prioritizes
version-specific properties; if a version-specific definition of the property
exists, the tool will use it. Otherwise, it will default to the generic one.
