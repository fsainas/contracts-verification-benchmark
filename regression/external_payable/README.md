# Payable

## Specification
We have the contract `ExternalPayable` and the interface `I`.
### I interface
`I` is an interface and it defines an external payable function `f`
```
interface I {
	function f() external payable;
}
```

### ExternalPayable contract

The contract `ExternalPayable` has two functions `g` and `balanceOf`: 

- the function `g` calls the funcion `f` from interface `i` and transfers 10 wei. The function `g` can only be called if the balance of the contract is equal to 100 wei.
    ```
    function g(I i) public {
		require(address(this).balance == 100);
		i.f{value: 10}();
	}
    ```
- the function `balanceOf` returns the balance of the address `a`.
    ```
    function balanceOf(address a) public view returns (uint){
        return a.balance;
    }
    ```

## Properties
- **g-check-balance**: after calling the function `g()` the contract balance is decreased by 10

## Ground truth
|        | g-check-balance |
|--------|-----------------|
| **v1** | 0[^1]           |
 
[^1]: The calling contract might fail to send Ether, for example because the called contract calls revert()

## Experiments
### SolCMC
#### Z3
|        | g-check-balance |
|--------|-----------------|
| **v1** | TN!             |
 

#### ELD
|        | g-check-balance |
|--------|-----------------|
| **v1** | TN!             |
 


### Certora
|        | g-check-balance |
|--------|-----------------|
| **v1** | TN              |
 

