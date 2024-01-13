This contract involves three participants: a buyer, a seller and an arbiter. At construction, the buyer provides a deposit in ETH, and it specifies the addresses of the seller and of the arbiter, and the fee that will be paid to the arbiter in case it is used to resolve a dispute. After construction, the contract operates in three states: Agree, Dispute, Redeem. 

In the Agree state, one of three things may happen: 
- the buyer approves the payment to the seller; 
- the seller issues a full refund to the buyer;
- either the buyer or the seller open a dispute.

In case a dispute is open, the arbiter takes the fee, and chooses whom between the buyer and the seller can redeem the residual funds. After the arbiter choice, the chosen recipient can redeem the funds.