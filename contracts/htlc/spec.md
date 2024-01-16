The Hash Timed Locked Contract (HTLC) involves two users, the *owner* and the *verifier*, and it allows the owner to commit to a secret and reveal it afterwards, within a given deadline. 

The commitment is the SHA256 digest of the secret (a bitstring). At contract creation, the owner specifies the verifier, who will receive the collateral in case the deposit is not revealed within the deadline. 

The deadline expires 1000 blocks after the block where the contract has been deployed: if deployment is at block N, `timeout` can be called in a block with height strictly greater than N+1000.

After contract creation, the HTLC allows the following actions:
- `commit` requires the owner to deposits a collateral (at least 1 ETH) in the contract, and records the commitment;
- `reveal` allows the owner to withdraw the whole contract balance, by revealing a preimage of the committed secret;
- `timeout` can be called by anyone only after the deadline, and tranfers the whole contract balance to the verifier.