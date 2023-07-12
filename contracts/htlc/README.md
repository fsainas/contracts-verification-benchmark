# HTLC

## Specification
The Hash Timed Locked Contract (HTLC) involves two users, the *committer* and the *verifier*,
and it allows the committer to commit a secret and reveal it afterwards, within a given deadline.
The commit is the SHA256 digest of the secret (a bitstring).
At contract creation, the committer specifies the receiver of the collateral, 
in case the deposit is not revealed within the deadline.
The deadline expires 1000 blocks after the block where the contract has been deployed:
if deployment is at block N, `timeout` can be called in a block with height strictly greater
than N+1000.

After contract creation, the HTLC allows the following actions:
- `commit` requires the committer to deposits a collateral (at least 1 ETH) in the contract,
and records the commit;
- `reveal` allows the committer to withdraw the whole contract balance,
  by revealing a preimage of the committed secret;
- `timeout` can be called by anyone only after the deadline, and
  and tranfers the whole contract balance to the receiver.


## Properties

- **p1**: the overall sent amount does not exceed the initial deposit.
  This property should always be false, since a contract can receive ETH
  when its address is specified in a coinbase transaction or in a `selfdestruct`.
- **p2**: `reveal` and `timeout` can only be called after `commit`.
- **p3**: if `timeout` is called, then at least 1000 blocks have passed since the contract was deployed.
- **p4**: if `commit` is called, then the sender must be the committer.


## Versions

- **v1**: conformant to specification.
- **v2**: removed check that `commit` must be called before `reveal` and `timeout`.
- **v3**: `timeout` can be called since block N+1000 (included).
- **v4**: `timeout` transfers balance to `msg.sender` instead of verifier.


## Experiments

### SolCMC

|        | p1  | p2  | p3  | p4  |
| ------ | --- | --- | --- | --- |
| **v1** | TN  | TP  | TP  | TN  |
| **v2** | TN  | TN  | TP  | TN  |
| **v3** | TN  | TP  | TN  | TN  |
| **v4** | TN  | TP  | TP  | TN  |
