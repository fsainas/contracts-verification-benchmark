# Zero Token Bet
## Specification
The contract involves two players, each owning 1 token, and an oracle. Player A initiates the contract by depositing its token. Then, player B can deposit its token. Once both players have deposited their token, the oracle chooses the winner, which receives the 2 tokens. After a given time limit, it is only possibile for both players to take their tokens back, if any. In this contract, tokens are stored in contract fields.

## Properties
- **ab-gte0**: the balance of player A is always nonnegative
- **ab-lte2**: the balance of player A does not exceed 2 tokens
- **bb-gte0**: the balance of player B is always nonnegative
- **bb-lte2**: the balance of player B does not exceed 2 tokens
- **candep**: before the deadline, if B has at least 1 token and he has not joined the bet yet, then he can deposit 1 token in the contract
- **cannotdep**: if B has less than 1 token or he has already joined the bet, then he cannot deposit 1 token in the contract
- **cb-gte0**: the contract balance is always nonnegative
- **cb-lte2**: the contract balance does not exceed 2 tokens

## Versions
- **v1**: compliant with the specification.
- **v2**: deposit() omits require enforcing a single call.

## Ground truth
|        | ab-gte0   | ab-lte2   | bb-gte0   | bb-lte2   | candep    | cannotdep | cb-gte0   | cb-lte2   |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **v1** | 1         | 1         | 1         | 1         | 1         | 1         | 1         | 1         |
| **v2** | 1         | 0         | 0         | 1         | 1         | 0         | 1         | 0         |
 

## Experiments
### SolCMC
|        | ab-gte0   | ab-lte2   | bb-gte0   | bb-lte2   | candep    | cannotdep | cb-gte0   | cb-lte2   |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **v1** | TP!       | TP!       | TP!       | TP!       | TP!       | TP!       | TP!       | TP!       |
| **v2** | TP!       | TN!       | TN!       | FN        | TP!       | TN!       | TP!       | TN!       |
 

### Certora
|        | ab-gte0   | ab-lte2   | bb-gte0   | bb-lte2   | candep    | cannotdep | cb-gte0   | cb-lte2   |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **v1** | TP!       | FN!       | TP!       | FN!       | TP!       | FN!       | TP!       | FN!       |
| **v2** | TP!       | TN!       | TN!       | FN!       | TP!       | TN!       | TP!       | TN!       |
 
