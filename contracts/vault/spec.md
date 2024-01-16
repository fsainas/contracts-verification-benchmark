Vaults are a security mechanism to prevent cryptocurrency from being immediately withdrawn by an adversary who has stolen the owner's private key. To create the vault, the owner specifies a recovery key (distinct from the primary owner key), which can be used to cancel a withdraw request, and a wait time that has to elapse between a withdraw request and the actual currency transfer to the chosen recipient. 

Once the contract has been created, anyone can deposit native cryptocurrency in the vault through an external transaction.

The contract can be in one of two states:
- IDLE: the vault is waiting for a withdraw request;
- REQ: the owner has issued a `withdraw` request that has not been finalized yet. In this state, the owner can choose to `finalize` the request or to `cancel` it. Finalization can only happen after the wait time has passed since the request. During the wait time, the request can be cancelled by using the recovery key.

Concretely, the keys are represented as addresses: requiring that an action can only be performed by someone knowing a certain key corresponds to requiring that a method is called by the corresponding address.