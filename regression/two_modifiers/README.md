# TwoModifiers

## Specification
The contract `TwoModifiers` has a modifier `m` that takes an input parameter `z`:
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

The contract has also two functions `f` and `g`. The function `f` is marked as internal and calls the modifier `m` with input `10` and `12`. The function `g` sets the value of `x` to `0` and calls the function `f`.
```
function f() m(10) m(12) internal {
    x = 3;
}
function g() public {
    x = 0;
    f();
}
```

The correct property is `f-modifiers-x-right` because before the function `f` is executed, the modifiers are evaluated up to the `_` symbol and, once the function body has finished, it will continue to execute the modifiers in reverse order.

## Properties
- **g-modifiers-x-right**: x equals to 7 after the call to `g`
- **g-modifiers-x-wrong**: x equals to 3 after the call to `g`

## Ground truth
|        | g-modifiers-x-right | g-modifiers-x-wrong |
|--------|---------------------|---------------------|
| **v1** | 1                   | 0                   |
 

## Experiments
### SolCMC
#### Z3
|        | g-modifiers-x-right | g-modifiers-x-wrong |
|--------|---------------------|---------------------|
| **v1** | FN!                 | FP!                 |
 

#### ELD
|        | g-modifiers-x-right | g-modifiers-x-wrong |
|--------|---------------------|---------------------|
| **v1** | FN!                 | FP!                 |
 


### Certora
|        | g-modifiers-x-right | g-modifiers-x-wrong |
|--------|---------------------|---------------------|
| **v1** | TP!                 | TN                  |
 

