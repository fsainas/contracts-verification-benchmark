# Vault

## Specification

Vaults are a security mechanism to prevent cryptocurrency from being
immediately withdrawn by an adversary who has stolen the owner's private key.
To create the vault, the owner specifies a recovery key (distinct from the primary owner key),
which can be used to cancel a withdraw request, and a wait time that has to elapse between a
withdraw request and the actual currency transfer to the chosen recipient.
Once the contract has been created, anyone can deposit native cryptocurrency in the vault
through an external transaction.

The contract can be in one of two states:
- IDLE: the vault is waiting for a withdraw request;
- REQ: the owner has issued a withdraw request that has not been finalized yet.
  In this state, the owner can choose to **finalize** the request or to **cancel** it.
  Finalization can only happen after the wait time has passed since the request.
  During the wait time, the request can be cancelled by using the recovery key.


## Properties

- **p1**: `withdraw()` and `finalize()` can only be called with the owner key;
- **p2**: `cancel()` can only be called with the recovery key;
- **p3**: the current state and the previous state alternate between IDLE and REQ;
- **p4**: if there is a withdraw request then the amount is positive and fully
  covered by the contract balance;
- **p5**: the owner key is never equal to the recovery key.


## Versions

- **v1**: conforming to specification;
- **v2**: require in constructor wrongly uses state variable instead of parameter.
- **v3**: require in `withdraw()` wrongly uses state variable instead of parameter.


## Experiments

### SolCMC

|        | p1  | p2  | p3  | p4  | p5  |
| ------ | --- | --- | --- | --- | --- |
| **v1** | TP  | TP  | TP  | TP  | TP  |
| **v2** | TP  | TP  | TP  | TP  | TN  |
| **v3** | TP  | TP  | TP  | TN  | TP  |

