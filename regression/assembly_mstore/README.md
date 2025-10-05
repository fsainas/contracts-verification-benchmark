# Assembly Mstore

## Specification
The contract defines the struct `S` as:
```
struct S {
    uint x;
}
```
And the function `f` that executes inline assembly to change the value of `sm.x` with the value `i`:
```
function f() public {
    s.x = 42;
    S memory sm = s;
    uint256 i = 7;
    assembly {
        mstore(sm, i)
    }
    s = sm;
}
```

The property `struct-store` should pass since we know the value `i`.

## Properties
- **struct-store**: after the call to the function `f`, the variable `s.x` is equal to 7.

## Ground truth
|        | struct-store |
|--------|--------------|
| **v1** | 1            |
 

## Experiments
### SolCMC
#### Z3
|        | struct-store |
|--------|--------------|
| **v1** | FN!          |
 

#### ELD
|        | struct-store |
|--------|--------------|
| **v1** | FN!          |
 


### Certora
|        | struct-store |
|--------|--------------|
| **v1** | TP!          |
 

