# Escrow
## Specification
This contract involves three participants: a buyer, a seller and an arbiter. At construction, the buyer provides a deposit in ETH, and it specifies the addresses of the seller and of the arbiter, and the fee that will be paid to the arbiter in case it is used to resolve a dispute. After construction, the contract operates in three states: Agree, Dispute, Redeem. 

In the Agree state, one of three things may happen: 
- the buyer approves the payment to the seller (method `approve_payment`); 
- the seller issues a full refund to the buyer (method `refund`);
- either the buyer or the seller open a dispute (method `open_dispute`).

The first two actions transition the state to Redeem, while the latter leads to Dispute.

In the Dispute state, the arbiter redeems the fee, and chooses whom between the buyer and the seller can redeem the residual funds. After the arbiter choice, the state transitions to Redeem. 

In the Redeem state, the chosen recipient can `redeem` the whole contract balance.

## Properties
- **arbitrate-send**: after a successful call to `arbitrate`, the arbiter receives `fee` ETH.
- **auth-in-agree**: in the Agree state, only the buyer and the seller can perform actions.
- **auth-in-dispute**: in the Dispute state, only the arbiter can perform actions.
- **dispute-if-agree**: in the Agree state, both the buyer and the seller can open a dispute.
- **dispute-onlyif-agree**: a dispute can be opened only in the Agree state.
- **no-send-in-agree**: in the Agree state, no one can redeem ETH.
- **recipient-buyer-or-seller**: the recipient of the `redeem` call must be either the buyer or the seller.
- **redeem-send**: after a successful call to `redeem`, either the buyer or the seller receives `deposit` ETH.

## Versions
- **v1**: conformant to specification.
- **v2**: allow arbitrate in any state.

## Ground truth
|        | arbitrate-send            | auth-in-agree             | auth-in-dispute           | dispute-if-agree          | dispute-onlyif-agree      | no-send-in-agree          | recipient-buyer-or-seller | redeem-send               |
|--------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| **v1** | 1                         | 1                         | 1                         | 1                         | 1                         | 1                         | 1                         | 1                         |
| **v2** | 1                         | 0                         | 1                         | 1                         | 1                         | 0                         | 1                         | 1                         |
 


## Experiments
                   |
 
### SolCMC
|        | arbitrate-send            | auth-in-agree             | auth-in-dispute           | dispute-if-agree          | dispute-onlyif-agree      | no-send-in-agree          | recipient-buyer-or-seller | redeem-send               |
|--------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| **v1** | ND                        | TP!                       | TP!                       | FN!                       | TP!                       | TP!                       | TP!                       | ND                        |
| **v2** | ND                        | TN!                       | TP!                       | FN!                       | TP!                       | TN                        | TP!                       | ND                        |
 


### Certora
|        | arbitrate-send            | auth-in-agree             | auth-in-dispute           | dispute-if-agree          | dispute-onlyif-agree      | no-send-in-agree          | recipient-buyer-or-seller | redeem-send               |
|--------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| **v1** | ND                        | TP!                       | TP!                       | TP!                       | TP!                       | TP!                       | FN!                       | ND                        |
| **v2** | ND                        | TN!                       | TP!                       | TP!                       | TP!                       | TN!                       | FN!                       | ND                        |
 
