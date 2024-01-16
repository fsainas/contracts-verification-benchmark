
# Vault
## Specification
Vaults are a security mechanism to prevent cryptocurrency from being immediately withdrawn by an adversary who has stolen the owner's private key. To create the vault, the owner specifies a recovery key (distinct from the primary owner key), which can be used to cancel a withdraw request, and a wait time that has to elapse between a withdraw request and the actual currency transfer to the chosen recipient. Once the contract has been created, anyone can deposit native cryptocurrency in the vault through an external transaction.

The contract can be in one of two states:

- IDLE: the vault is waiting for a withdraw request;

- REQ: the owner has issued a withdraw request that has not been finalized yet. In this state, the owner can choose to **finalize** the request or to **cancel** it. Finalization can only happen after the wait time has passed since the request. During the wait time, the request can be cancelled by using the recovery key. 

Concretely, the keys are represented as addresses: requiring that an action can only be performed by someone knowing a certain key corresponds to requiring that a method is called by the corresponding address.

## Properties
- **p1**: calling `withdraw` or `finalize` with a key different from the owner key, reverts.
- **p2**: calling `cancel` with a key different from the recovery key, reverts.
- **p3**: `withdraw` may be called twice in a row.
- **p4**: `finalize` or `cancel` may be called after `finalize` or `cancel`.
- **p5**: the owner key is never equal to the recovery key.
- **p6**: after a successful `withdraw`, `finalize` may be successfully called before `wait_time` blocks have elapsed, with no in-between calls.
- **p7**: after a successful `withdraw`, `finalize` may be successfully called before `wait_time` blocks have elapsed, possibly with in-between calls.
- **p8**: if an actor holds the recovery key, they can always prevent other actors from withdrawing funds from the contract
- **p9**: if an actor holds both the owner and recovery key, and no one else knows the recovery key, the former is able to eventually withdraw all the contract balance with probability 1 (for every fair trace).

## Versions
- **v1**: conforming to specification.
- **v2**: require in constructor wrongly uses state variable instead of parameter.
- **v3**: removed the time constraint on `finalize`.

## Ground truth
|        | p1  | p2  | p3  | p4  | p5  | p6  | p7  | p8  | p9  |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **v1** | 1   | 1   | 0   | 0   | 1   | 0   | 0   | 1   | 1   |
| **v2** | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   |
| **v3** | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 0   |


## Experiments

### SolCMC
|        | p1    | p2    | p3    | p4    | p5    | p6    | p7    | p8    | p9    |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **v1** | TP!   | TP!   | ND    | ND    | ND    | ND    | ND    | ND    | ND    |
| **v2** | TP!   | TP!   | ND    | ND    | ND    | ND    | ND    | ND    | ND    |
| **v3** | TP!   | TP!   | ND    | ND    | ND    | ND    | ND    | ND    | ND    |

### Certora
|        | p1  | p2  | p3  | p4  | p5  | p6  | p7  | p8  | p9  |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **v1** | TP! | TP! | TN! | TN! | TP! | TN! | ND  | ND  | ND  |
| **v2** | TP! | TP! | TN! | TN! | TN! | TN! | ND  | ND  | ND  |
| **v3** | TP! | TP! | TN! | TN! | TP! | TP! | ND  | ND  | ND  |
