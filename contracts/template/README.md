# Usecase Name
## Specification
Usecase specification.

## Properties
- **bar**: x is not equal to another value
- **foo**: x is equal to the initial value

## Versions
- **v1**: version 1
- **v2**: version 2

## Ground truth
|        | bar   | foo   |
|--------|-------|-------|
| **v1** | 1     | 1[^1] |
| **v2** | 1     | 1     |
 
[^1]: Footnote foo-v1

## Experiments
### SolCMC
|        | bar   | foo   |
|--------|-------|-------|
| **v1** | ND    | TP!   |
| **v2** | TP!   | TP!   |
 

### Certora
|        | bar   | foo   |
|--------|-------|-------|
| **v1** | ND    | FN!   |
| **v2** | ND    | FN!   |
 
