# Vault

## Specification

Vaults are a security mechanism to prevent cryptocurrency from being
immediately withdrawn by an adversary who has stolen the owner's private key.
To create the vault, the owner specifies a recovery key, which can be used to
cancel a withdraw request, and a wait time that has to elapse between a
withdraw request and the actual currency transfer. Once the vault contract have
been created, anyone can deposit native cryptocurrency.

When users want to withdraw from a vault, they must first issue a request. The
withdrawal is finalized only after the wait time has passed since the request.
During the wait time, the request can be cancelled by using a recovery key.

The contract operates in two states: 'idle' and 'request' $\{I, R\}$.

## Versions

- **v1**: conformant to specification
- **v2**: adds two new states: 'paid' and 'cancel' $\{P, C\}$

## Properties

- **p1**: $p_0$ is the previous state, $p_1$ is the current one:
    - $p_0 = R \implies p_1 = P \lor p_1 = C$, if the previous state was 'request', the current one is either 'paid' or 'cancel'
    - $p_0 = P \lor p_0 = C \implies p_1 = R$, if the previous state was 'paid' or 'cancel', the current one is 'request'
    - $p_0 = p_1 \implies p_0 = I$, if the previous state is equal to the current one, the previous state is 'idle'

## Experimens

|        | p1                 |
| ------ | ------------------ |
| **v1** | 
| **v2** | :heavy_check_mark: |
