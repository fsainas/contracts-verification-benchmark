# Payable

## Specification
The contract `Payable` has two functions `g` and `balanceOf`: 

- the `g` function calls the contract at address `i` and transfers 10 wei. The function `g` can only be called if the balance of the contract is equal to 100 wei.
    ```
    function g(address payable i) public {
        require(address(this).balance == 100);
        i.call{value: 10}("");
    }
    ```
- the `balanceOf` function returns the balance of the address `a`.
    ```
    function balanceOf(address a) public view returns (uint){
        return a.balance;
    }
    ```

## Properties
- **g-check-balance**: checks that the function `g()` transfers the correct amount of ether

## Ground truth
|        | g-check-balance |
|--------|-----------------|
| **v1** | 1               |
 

## Experiments
### SolCMC
#### Z3
|        | g-check-balance |
|--------|-----------------|
| **v1** | TP!             |
 

#### ELD
|        | g-check-balance |
|--------|-----------------|
| **v1** | FN              |
 


### Certora
|        | g-check-balance |
|--------|-----------------|
| **v1** | FN              |
 

