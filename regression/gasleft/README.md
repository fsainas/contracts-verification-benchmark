# GasLeft

## Specification
The contract `GasLeft` has a function `f` that calls `gasleft` twice so that we can check that the gas left decreases after each call.
```
function f() public {
    uint g = gasleft();
    gasleft();
}
```

## Properties
- **less-equal-gasleft-assignment**: There is less or equal gas left after the assignment
- **more-gasleft-assignment**: There is more gas left after the assignment

## Ground truth
|        | less-equal-gasleft-assignment | more-gasleft-assignment       |
|--------|-------------------------------|-------------------------------|
| **v1** | 1                             | 0                             |
 

## Experiments
### SolCMC
#### Z3
|        | less-equal-gasleft-assignment | more-gasleft-assignment       |
|--------|-------------------------------|-------------------------------|
| **v1** | TP!                           | TN!                           |
 

#### ELD
|        | less-equal-gasleft-assignment | more-gasleft-assignment       |
|--------|-------------------------------|-------------------------------|
| **v1** | TP!                           | TN!                           |
 


### Certora
|        | less-equal-gasleft-assignment | more-gasleft-assignment       |
|--------|-------------------------------|-------------------------------|
| **v1** | FN                            | TN                            |
 

