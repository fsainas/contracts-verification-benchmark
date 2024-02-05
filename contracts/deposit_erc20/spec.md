This contract implements the same functionality of the [Deposit contract](../deposit_eth), but operates on ERC20 tokens instead of ETH. 

The `constructor` takes the token address as a parameter. 

The `deposit` function allows the sender to deposit an arbitrary number of token units into the contract; it can be called only once. Before calling `deposit`, the depositor must approve that the amount they want to deposit can be spent by the contract: if so, the entire allowance is transferred to the contract.

The function `withdraw(amount)` can be called by anyone to transfer `amount` token units to the transaction sender.