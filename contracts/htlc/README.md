# HTLC

## Specification

The Hash Timed Locked Contract (HTLC) involves two users,
allows one participant to commit to a secret and reveal it afterwards.
The commit is the SHA256 digest of the secret (a bitstring).
Upon contract creation, the committer:
- deposits a collateral (in native cryptocurrency) in the contract;
- specifies a deadline for the secret revelation;
- specifies the receiver of the collateral, 
in case the deposit is not revealed within the deadline.

Upon contract creation, the HTLC allows two actions:
- `reveal`, which requires the caller to provide a preimage of the commit,
and tranfers the whole contract balance to the committer;
- `timeout`, which can be called only after the deadline, and
and tranfers the whole contract balance to the receiver.

## Versions

- **v1**: conformant to the specification

## Invariants

- **p1**: amount sent does not exceed deposit
- **p2**: `reveal` and `timeout` can only be called after `commit`
