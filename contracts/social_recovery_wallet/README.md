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

## Versions
- **v1**: conformant to specification
- **v2**: removed guardian management

## Properties
- **p1**: the first owner is always the owner, in other words: the owner cannot
  change (should fail)
- **p2**: the recovery can never happen (should fail)
- **p3**: if `address(0x1)` has initiated or supported a recovery, then
  `address(0x1)` is a guardian (should fail in v1)
- **p4**: if two guardians have selected the same new owner, the round is 1 and
  the threshold is 2, then `executeRecovery()` will succeed
- **p5**: `executeRecovery()` will fail if not enough guardians joined the
  recovery process

## Experiments


|        | p1                 | p2                 | p3         | p4         | p5                 |
| ------ | ------------------ | ------------------ | ---------- | ---------- | ------------------ |
| **v1** | :white_check_mark: | :white_check_mark: | :question: | :question: | :heavy_check_mark: |
| **v2** |                    |                    | :question: | :question: |                    |
