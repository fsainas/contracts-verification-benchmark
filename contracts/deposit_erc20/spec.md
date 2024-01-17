This contract implements the same functionality of [Deposit contract](../deposit_eth), but operates on ERC20 tokens instead of ETH. 

The `constructor` takes the token address as a parameter. 

The `deposit` function allows the sender to deposit an arbitrary number of token units into the contract; it can be called only once. Before calling `deposit`, the depositor must approve that the amount they want to deposit can be spent by the contract: if so, the entire allowance is transferred to the contract.

With ERC20 tokens, one can easily increase the contract balance without the contract being able to notice or prevent it. Since this is also possible with ETH (via coinbase or `selfdestruct` transactions), the behavior is comparable for the purposes of these tests.

The contract has a `withdraw` function that can be called by anyone and transfers  `amount` token units (specified as a parameter) to the transaction sender.