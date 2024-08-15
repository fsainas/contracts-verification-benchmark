The contract `Payable` has two functions `g` and `balanceOf`: 

- the function `g` calls the contract at address `i` and transfers 10 wei. The function `g` can only be called if the balance of the contract is equal to 100 wei.
    ```
    function g(address payable i) public {
        require(address(this).balance == 100);
        i.call{value: 10}("");
    }
    ```
- the function `balanceOf` returns the balance of the address `a`.
    ```
    function balanceOf(address a) public view returns (uint){
        return a.balance;
    }
    ```