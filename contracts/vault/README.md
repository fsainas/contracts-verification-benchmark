# Vault

## Specification
Vaults are a security mechanism to prevent cryptocurrency from being immediately withdrawn by an adversary who has stolen the owner's private key. To create the vault, the owner specifies a recovery key (distinct from the primary owner key), which can be used to cancel a withdraw request, and a wait time that has to elapse between a withdraw request and the actual currency transfer to the chosen recipient. 

Once the contract has been created, anyone can deposit native cryptocurrency in the vault through an external transaction.

The contract can be in one of two states:
- IDLE: the vault is waiting for a withdraw request;
- REQ: the owner has issued a `withdraw` request that has not been finalized yet. In this state, the owner can choose to `finalize` the request or to `cancel` it. Finalization can only happen after the wait time has passed since the request. During the wait time, the request can be cancelled by using the recovery key.

Concretely, the keys are represented as addresses: requiring that an action can only be performed by someone knowing a certain key corresponds to requiring that a method is called by the corresponding address.

## Properties
- **canc-revert**: calling `cancel` with a key different from the recovery key, reverts.
- **fin-canc-twice**: `finalize` or `cancel` may be called immediately after `finalize` or `cancel`.
- **okey-neq-rkey**: the owner key is never equal to the recovery key.
- **okey-rkey-private-wd**: if an actor holds both the owner and recovery key, and no one else knows the recovery key, the former is able to eventually withdraw all the contract balance with probability 1 (for every fair trace).
- **rkey-no-wd**: if an actor holds the recovery key, they can always prevent other actors from withdrawing funds from the contract
- **wd-fin-before**: after a successful `withdraw`, `finalize` may be successfully called before `wait_time` blocks have elapsed, with no in-between calls.
- **wd-fin-before-interleave**: after a successful `withdraw`, `finalize` may be successfully called before `wait_time` blocks have elapsed, possibly with in-between calls.
- **wd-fin-revert**: calling `withdraw` or `finalize` with a key different from the owner key, reverts.
- **wd-twice**: `withdraw` cannot be called twice in a row.

## Versions
- **v1**: conforming to specification.
- **v2**: require in constructor wrongly uses state variable instead of parameter.
- **v3**: removed the time constraint on `finalize`.

## Ground truth
|        | canc-revert              | fin-canc-twice           | okey-neq-rkey            | okey-rkey-private-wd     | rkey-no-wd               | wd-fin-before            | wd-fin-before-interleave | wd-fin-revert            | wd-twice                 |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | 1                        | 0                        | 1                        | 1                        | 1                        | 0                        | 0                        | 1                        | 1                        |
| **v2** | 1                        | 0                        | 0                        | 1                        | 1                        | 0                        | 0                        | 1                        | 1                        |
| **v3** | 1                        | 0                        | 1                        | 0                        | 0                        | 1                        | 1                        | 1                        | 1                        |
 

## Experiments
### SolCMC
#### Z3
|        | canc-revert              | fin-canc-twice           | okey-neq-rkey            | okey-rkey-private-wd     | rkey-no-wd               | wd-fin-before            | wd-fin-before-interleave | wd-fin-revert            | wd-twice                 |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | TP!                      | ND                       | TP!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
| **v2** | TP!                      | ND                       | TN!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
| **v3** | TP!                      | ND                       | TP!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
 

#### Eldarica
|        | canc-revert              | fin-canc-twice           | okey-neq-rkey            | okey-rkey-private-wd     | rkey-no-wd               | wd-fin-before            | wd-fin-before-interleave | wd-fin-revert            | wd-twice                 |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | TP!                      | ND                       | TP!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
| **v2** | TP!                      | ND                       | TN!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
| **v3** | TP!                      | ND                       | TP!                      | ND                       | ND                       | ND                       | ND                       | TP!                      | ND                       |
 


### Certora
|        | canc-revert              | fin-canc-twice           | okey-neq-rkey            | okey-rkey-private-wd     | rkey-no-wd               | wd-fin-before            | wd-fin-before-interleave | wd-fin-revert            | wd-twice                 |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **v1** | TP!                      | TN!                      | TP!                      | ND                       | ND                       | TN!                      | ND                       | TP!                      | TP!                      |
| **v2** | TP!                      | TN!                      | TN                       | ND                       | ND                       | TN!                      | ND                       | TP!                      | TP!                      |
| **v3** | TP!                      | TN!                      | TP!                      | ND                       | ND                       | TP                       | ND                       | TP!                      | TP!                      |
 

