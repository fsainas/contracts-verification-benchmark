# Social Recovery Wallet

This is a simplified version of
[this](https://github.com/verumlotus/social-recovery-wallet/blob/main/src/Wallet.sol)
contract by [@verumlotus](https://github.com/verumlotus). 

The concept was popularized by
[this](https://vitalik.ca/general/2021/01/11/recovery.html) article by Vitalik
Buterin.

## Specification

This wallet can be used by the owner to make transactions by calling the
`executeExternalTx()` function, by provinding the desired recipient
contract/externally owned account (EOA), an ether value, and arbitrary data.

In case of lost private key, a recovery process can be initiated by a guardian.
The guardian first calls `initiateRecovery()` with the address of the new
owner, followed by a threshold number of guardians calling `supportRecovery()`
with the new owner's address. Finally, any guardian can call
`executeRecovery()` to change the wallet's owner. 

Additionally, owners have the ability to manage guardians by removing
compromised or malicious guardians. The owner initiates the removal process by
calling `initiateGuardianRemoval()` with the hash of the guardian's address,
which queues the guardian for removal after a 3-day delay. The owner then calls
`executeGuardianRemoval()` after the delay, providing the hash of a new
guardian's address to finalize the removal and add the new guardian.
Alternatively, the owner can call `cancelGuardianRemoval()` to restore the
guardian state.

## Properties

- **p1**: the first owner is always the owner, in other words: the owner cannot
  change (should fail)
- **p2**: the recovery can never happen (should fail)
- **p3**: if an address `addr` has participated in a recovery, then `addr` is a
  guardian. Should fail in v1 because guardians can be removed
- **p4**: if number of guardian greater than or equal to the threshold has
  participated in the same recovery round, and selected the same new owner,
  then `executeRecovery()` will succeed and `owner == newOwner`
- **p5**: `executeRecovery()` will fail if not enough guardians have joined the
  recovery process

## Versions

- **v1**: conformant to specification
- **v2**: removed guardian management

## Experiments

### SolCMC

|        | p1  | p2  | p3  | p4  | p5  |
| ------ | --- | --- | --- | --- | --- |
| **v1** | TN  | TN  | ?   | ?   | ?   |
| **v2** |     |     | ?   |     | ? 
