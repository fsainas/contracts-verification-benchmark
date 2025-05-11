# Benchmark Toolchain

## Table of Contents
- [Structure](#structure)
- [Testing](#testing)

## Structure
The toolchain consists of three main packages:

1. [`setup`](#setup-package): Modules related to setting up experiments.
1. [`tools`](#tools-package): Modules to run experiments with various verification tools.
1. [`report_gen`](#report-gen-package): Modules to generate reports on experiments.

To interact with the functionality provided by the toolchain, there are several
interface scripts designed to be executed directly from the command line. These
scripts act as entry points to access different features of the toolchain.
Interface scripts reside at the top level directory.

### Interface Scripts
- `builder.py`: Instruments contracts in `versions/` with Solcmc code.
- `inject_getters.py`: Injects getters into contracts to be verified with Certora.
- `run_solcmc.py`: Runs Solcmc experiments.
- `run_certora.py`: Runs Certora experiments.
- `cm_gen.py`: Generates the confusion matrix of experiments results.
- `mdtable_gen.py`: Turns a csv file into a markdown table.
- `readme_gen.py`: Generates the plain README.md (specifications and ground-truth).
- `score.py`: Computes the benchmark scores.

### Setup Package
- `injector.py`: Functions to inject code.
- `instrumentation.py`: Functions to instrument contracts with Solcmc code.

### Tools Package
- `solcmc.py`: Functions to run Solcmc experiments.
- `certora.py`: Functions to run Certora experiments.
- `hardhat.py`: Functions to run Hardhat PoC (Proof of Concept).

### Report Gen Package
- `cm.py`: Funcitons to generate a confusion matrix.
- `mdtable.py`: Functions to convert a csv to a markdown table.
- `readme.py`: Functions to generate the plain README.md (specifications and ground-truth)
- `scoring.py`: Functions to compute the score of tools.

## Testing
### Dependencies
Before running tests, ensure that `pytest` is installed. You can install it via
pip using the following command:
```
$ pip install pytest
```

### Tests Structure
The tests are located under the `test/` directory. Each file within this
directory corresponds to a specific module.

Tests are written using the `unittest` framework. Within each test file, test
classes are utilized to test individual functions.

### Running Tests
To execute the tests, simply run the following command under the `script/`
directory:
```
$ make
```
