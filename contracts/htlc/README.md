# HTLC

## Specification

The Hash Timed Locked Contract (HTLC) involves two users, and it
allows one participant to commit to a secret and reveal it afterwards.
The commit is the SHA256 digest of the secret (a bitstring).
At contract creation, the committer
specifies the receiver of the collateral, 
in case the deposit is not revealed within the deadline.

After contract creation, the HTLC allows the following actions:
- `commit`, requires the committer to deposits a collateral
(in native cryptocurrency) in the contract, and records the commit;
- `reveal`, which requires the caller to provide a preimage of the commit,
and tranfers the whole contract balance to the committer;
- `timeout`, which can be called only after the deadline, and
and tranfers the whole contract balance to the receiver.


## Versions

- **v1**: conformant to the specification
- **v2**: removed check that `commit` must be called before `reveal` and `timeout`

## Invariants

- **p1**: amount sent does not exceed deposit
- **p2**: `reveal` and `timeout` can only be called after `commit`


## Experiments

|       | p1 | p2 |   |
|-------|----|----|---|
| v1_p1 | 1  | -  |   |
| v1_p2 | -  | 1  |   |
| v2_p2 | -  | 0  |   |
