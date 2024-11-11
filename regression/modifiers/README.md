# Modifiers

## Specification
The contract `Modifiers` has a modifier `m` that takes an input parameter `z`:
```
modifier m(uint z) {
		uint y = 3;
        if (z == 10)
            x = 2 + y;
        _;
        if (z == 10)
            x = 4 + y;
    }
```

The contract has also two functions `f` and `g`. The function `f` is marked as internal and calls the modifier `m` with input `10`. The function `g` sets the value of `x` to `0` and calls the function `f`.
```
function f() m(10) internal {
    x = 3;
}
function g() public {
    x = 0;
    f();
}
```

## Properties
- **g-modifiers-x**: checks that x holds the correct value after the call to `g`

## Ground truth
|        | g-modifiers-x |
|--------|---------------|
| **v1** | 1             |
 

## Experiments
### SolCMC
#### Z3
|        | g-modifiers-x |
|--------|---------------|
| **v1** | TP!           |
 

#### ELD
|        | g-modifiers-x |
|--------|---------------|
| **v1** | TP!           |
 


### Certora
|        | g-modifiers-x |
|--------|---------------|
| **v1** | TP!           |
 

