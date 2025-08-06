# External abstract

## Specification
We have two contracts: `ExternalAbstract` and `D`.
### D contract
`D` is an abstract contract and it defines a virtual function `d` 
```
abstract contract D {
	function d() external virtual;
}
```

### ExternalAbstract contract
`ExternalAbstract` has two variables, `x` and `d`, and two functions, `f` and `g`.

- `x` is a uint variable.

- `d` is an instance of the contract `D`

- The function `f` increments `x` value by one if it is less than 10.
```
function f() public {
    if (x < 10)
        ++x;
}
```

- The function `g` requires `x` value to be less than 10, then performs an external call to `d.d`.
```
function g() public {
    require(x < 10);
    d.d();
}
```


We cannot trust `d.d` call because `d` could be implemented to call the function `f` of the `ExternalAbstract` contract.

## Properties
- **x-abstract-call**: after calling the function `d` from abstract contract `D`, `x` remains unchanged

## Ground truth
|        | x-abstract-call |
|--------|-----------------|
| **v1** | 0[^1]           |
 
[^1]: `x` can change because `d`'s code can call function `f`

## Experiments
### SolCMC
#### Z3
|        | x-abstract-call |
|--------|-----------------|
| **v1** | TN              |
 

#### ELD
|        | x-abstract-call |
|--------|-----------------|
| **v1** | TN!             |
 


### Certora
|        | x-abstract-call |
|--------|-----------------|
| **v1** | TN              |
 

