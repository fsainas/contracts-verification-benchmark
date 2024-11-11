# ThisPayable

## Specification
The contract `ThisPayable` has three functions `g`, `h` and `balanceOf`: 

- the function `g` calls the function `h` and transfers a custom amount of wei `i`. The function `g` can only be called if the balance of the contract is equal to 100 wei.
    ```
    function g(uint i) public {
        require(address(this).balance == 100);
        this.h{value: i}();
    }
    ```
- the function `h` is an external function that can receive ether
    ```
    function h() external payable {}
    ```
- the function `balanceOf` returns the balance of the address `a`.
    ```
    function balanceOf(address a) public view returns (uint){
        return a.balance;
    }
    ```

## Properties
- **g-check-balance**: after calling the function `g()` the contract balance remains unchanged

## Ground truth
|        | g-check-balance |
|--------|-----------------|
| **v1** | 1[^1]           |
 
[^1]: The balance is still the same as before the transaction because if i <= 100 then the contract sends wei to itself, otherwise it reverts and no wei is transferred.

## Experiments
### SolCMC
#### Z3
|        | g-check-balance |
|--------|-----------------|
| **v1** | TP!             |
 

#### ELD
|        | g-check-balance |
|--------|-----------------|
| **v1** | TP!             |
 


### Certora
|        | g-check-balance |
|--------|-----------------|
| **v1** | TP!             |
 

