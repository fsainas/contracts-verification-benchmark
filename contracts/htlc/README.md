# HTLC

## Specification
The Hash Timed Locked Contract (HTLC) involves two users, the *owner* and the *verifier*, and it allows the owner to commit to a secret and reveal it afterwards, within a given deadline. 

The commitment is the SHA256 digest of the secret (a bitstring). At contract creation, the owner specifies the verifier, who will receive the collateral in case the deposit is not revealed within the deadline. 

The deadline expires 1000 blocks after the block where the contract has been deployed: if deployment is at block N, `timeout` can be called in a block with height strictly greater than N+1000.

After contract creation, the HTLC allows the following actions:
- `commit` requires the owner to deposits a collateral (at least 1 ETH) in the contract, and records the commitment;
- `reveal` allows the owner to withdraw the whole contract balance, by revealing a preimage of the committed secret;
- `timeout` can be called by anyone only after the deadline, and tranfers the whole contract balance to the verifier.

## Properties
- **commit-auth-owner**: If `commit` is successfully called, then the sender must be the owner.
- **reveal-auth-owner**: If `reveal` is successfully called, then the sender must be the owner.
- **reveal-timeout-after-commit**: `reveal` and `timeout` can only be called after `commit`.
- **sent-le-init-bal**: The overall sent amount does not exceed the initial deposit.
- **timeout-deadline**: If `timeout` is called, then at least 1000 blocks have passed since the contract was deployed.

## Versions
- **v1**: conformant to specification.
- **v2**: removed check that `commit` can only be called before `reveal` and `timeout`.
- **v3**: `timeout` can be called since block N+999 (included).
- **v4**: `timeout` transfers balance to `msg.sender` instead of verifier.
- **v5**: removed check that `commit` can only be called by `owner`.
- **v6**: removed check that `reveal` can only be called by `owner`.

## Ground truth
|        | commit-auth-owner           | reveal-auth-owner           | reveal-timeout-after-commit | sent-le-init-bal            | timeout-deadline            |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | 1                           | 1                           | 1                           | 0[^1]                       | 1                           |
| **v2** | 1                           | 1                           | 0                           | 0                           | 1                           |
| **v3** | 1                           | 1                           | 1                           | 0                           | 0                           |
| **v4** | 1                           | 1                           | 1                           | 0                           | 1                           |
| **v5** | 0                           | 1                           | 1                           | 0                           | 1                           |
| **v6** | 1                           | 0[^2]                       | 1                           | 0                           | 1                           |
 
[^1]: This property should always be false, since a contract can receive ETH when its address is specified in a coinbase transaction or in a `selfdestruct`.
[^2]: Since the `reveal` transaction is broadcast in the mempool before the transaction is finalized, anyone can read the secret from the mempool and play its own `reveal` transaction.

## Experiments
### SolCMC
#### Z3
|        | commit-auth-owner           | reveal-auth-owner           | reveal-timeout-after-commit | sent-le-init-bal            | timeout-deadline            |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | TP!                         | TP!                         | TP!                         | TN!                         | TP!                         |
| **v2** | TP!                         | TP!                         | TN!                         | TN!                         | TP!                         |
| **v3** | TP!                         | TP!                         | TP!                         | TN!                         | TN!                         |
| **v4** | TP!                         | TP!                         | TP!                         | TN!                         | TP!                         |
| **v5** | TN!                         | TP!                         | TP!                         | TN!                         | TP!                         |
| **v6** | TP!                         | TN!                         | TP!                         | TN!                         | TP!                         |
 

#### Eldarica
|        | commit-auth-owner           | reveal-auth-owner           | reveal-timeout-after-commit | sent-le-init-bal            | timeout-deadline            |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | TP!                         | TP!                         | TP!                         | TN!                         | TP!                         |
| **v2** | TP!                         | TP!                         | UNK                         | UNK                         | TP!                         |
| **v3** | TP!                         | TP!                         | TP!                         | TN!                         | TN!                         |
| **v4** | TP!                         | TP!                         | TP!                         | TN!                         | TP!                         |
| **v5** | TN!                         | TP!                         | TP!                         | UNK                         | TP!                         |
| **v6** | TP!                         | TN!                         | TP!                         | TN!                         | TP!                         |
 


### Certora
|        | commit-auth-owner           | reveal-auth-owner           | reveal-timeout-after-commit | sent-le-init-bal            | timeout-deadline            |
|--------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| **v1** | TP!                         | FN                          | FN                          | TN                          | TP!                         |
| **v2** | TP!                         | FN                          | TN                          | TN                          | TP!                         |
| **v3** | TP!                         | FN                          | FN                          | TN                          | TN                          |
| **v4** | TP!                         | FN                          | FN                          | TN                          | TP!                         |
| **v5** | TN                          | FN                          | FN                          | TN                          | TP!                         |
| **v6** | TP!                         | TN                          | FN                          | TN                          | TP!                         |
 

