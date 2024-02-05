# Crowdfund

## Specification
The Crowdfund contract implements a crowdfunding campaign. 

The constructor specifies the `owner` of the campaign, the last block height where it is possible to receive donations (`end_donate`), and the `goal` in ETH that must be reached for the campaign to be successful. 

The contract implements the following methods:
- `donate`, which allows anyone to deposit any amount of ETH in the contract. Donations are only possible before the donation period has ended;
- `withdraw`, which allows the `owner` to redeem all the funds deposited in the contract. This is only possible if the campaign `goal` has been reached;   
- `reclaim`, which all allows donors to reclaim their donations after the donation period has ended. This is only possible if the campaign `goal` has not been reached.

## Properties
- **bal-decr-onlyif-wd-reclaim**: after the donation phase, if the contract balance decreases then either a successful `withdraw` or `reclaim` have been performed.
- **donate-not-revert**: a transaction `donate` is not reverted if the donation phase has not ended.
- **donate-not-revert-overflow**: a transaction `donate` is not reverted if the donation phase has not ended and sum between the old and the current donation does not overflow.
- **no-donate-after-deadline**: calls to `donate` will revert if the donation phase has ended.
- **no-receive-after-deadline**: the contract balance does not increase after the end of the donation phase.
- **no-wd-if-no-goal**: calls to `withdraw` will revert if the contract balance is less than the `goal`.
- **owner-only-recv**: only the owner can receive ETH from the contract.
- **reclaim-not-revert**: a transaction `reclaim` is not reverted if the goal amount is not reached and the deposit phase has ended, and the sender has donated funds that they have not reclaimed yet.
- **wd-not-revert**: a transaction `withdraw` is not reverted if the contract balance is greater than or equal to the goal and the donation phase has ended.
- **wd-not-revert-EOA**: a transaction `withdraw` is not reverted if the contract balance is greater than or equal to the goal, the donation phase has ended, and the `receiver` is an EOA.

## Versions
- **v1**: conforming to specification.

## Ground truth
|        | bal-decr-onlyif-wd-reclaim | donate-not-revert          | donate-not-revert-overflow | no-donate-after-deadline   | no-receive-after-deadline  | no-wd-if-no-goal           | owner-only-recv            | reclaim-not-revert         | wd-not-revert              | wd-not-revert-EOA          |
|--------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| **v1** | 1                          | 0[^1]                      | 1                          | 1                          | 0[^2]                      | 1                          | 1                          | 0[^3]                      | 0[^4]                      | 1                          |
 
[^1]: This property should be false, since the increment of the `donors` map could overflow.
[^2]: This property should always be false, since a contract can receive ETH when its address is specified in a coinbase transaction or in a `selfdestruct`.
[^3]: All funds may have been reclaimed already.
[^4]: Receiver of the funds may revert the transaction.

## Experiments
### SolCMC
#### Z3
|        | bal-decr-onlyif-wd-reclaim | donate-not-revert          | donate-not-revert-overflow | no-donate-after-deadline   | no-receive-after-deadline  | no-wd-if-no-goal           | owner-only-recv            | reclaim-not-revert         | wd-not-revert              | wd-not-revert-EOA          |
|--------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| **v1** | TP!                        | ND                         | ND                         | TP!                        | TN!                        | TP!                        | ND                         | ND                         | ND                         | ND                         |
 

#### Eldarica
|        | bal-decr-onlyif-wd-reclaim | donate-not-revert          | donate-not-revert-overflow | no-donate-after-deadline   | no-receive-after-deadline  | no-wd-if-no-goal           | owner-only-recv            | reclaim-not-revert         | wd-not-revert              | wd-not-revert-EOA          |
|--------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| **v1** | TP!                        | ND                         | ND                         | TP!                        | TN!                        | TP!                        | ND                         | ND                         | ND                         | ND                         |
 


### Certora
|        | bal-decr-onlyif-wd-reclaim | donate-not-revert          | donate-not-revert-overflow | no-donate-after-deadline   | no-receive-after-deadline  | no-wd-if-no-goal           | owner-only-recv            | reclaim-not-revert         | wd-not-revert              | wd-not-revert-EOA          |
|--------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| **v1** | TP!                        | TN                         | TP!                        | TP!                        | ND                         | TP!                        | TP!                        | TN                         | TN                         | FN                         |
 

