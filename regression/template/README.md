# Usecase Template

## Specification
Makefile usage:
- `make all`: run the benchmarking of all supported tools.
- `make solcmc`: run the benchmarking of solcmc (Z3 and Eldarica).
- `make certora`: run the benchmarking of certora.
- `make plain`: generate the README.md without experiments results.
- `make clean`: remove the README.md and files generated during experiments.

### Naming conventions
- Original contract: Name the original contract file by appending the version to the contract name (e.g. `C_v1.sol`).
- Solcmc contract: Name the contract instrumented for solcmc with the format: <contractName_property_version.sol> (e.g. `C_foo_v1.sol`). 
- Certora spec: Name the file according to the property name (e.g. `foo.spec`). 

Remember to adapt the makefile by changing the CONTRACT, SOLCMC_CONTRACT and CERTORA_SPEC paths.

Delete this text and write the description of your use case here.


## Properties
- **foo**: Contract balance is not zero when `f()` is called.

## Ground truth
|        | foo   |
|--------|-------|
| **v1** | 1     |
 

## Experiments
### SolCMC
#### Z3
|        | foo   |
|--------|-------|
| **v1** | TP!   |
 

#### ELD
|        | foo   |
|--------|-------|
| **v1** | TP!   |
 


### Certora
|        | foo   |
|--------|-------|
| **v1** | ERR   |
 

