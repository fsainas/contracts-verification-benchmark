The Crowdfund contract implements a crowdfunding campaign. 

The constructor specifies the `owner` of the campaign, the last block height where it is possible to receive donations (`end_donate`), and the `goal` in ETH that must be reached for the campaign to be successful. 

The contract implements the following methods:
- `donate`, which allows anyone to deposit any amount of ETH in the contract. Donations are only possible before the donation period has ended;
- `withdraw`, which allows the `owner` to redeem all the funds deposited in the contract. This is only possible if the campaign `goal` has been reached;   
- `reclaim`, which all allows donors to reclaim their donations after the donation period has ended. This is only possible if the campaign `goal` has not been reached.