# Zero Token Bet
## Specification
The contract involves three players and an oracle. Player A initiates the contract by depositing 1 token. Then, player B deposits 1 token. Once both players have placed their bet, an Oracle chooses the winner, which receives 2 tokens. If the Oracle does not choose within a given time, both players can take their tokens back. In this contract, tokens are just stored in contract fields.

## Properties
- **p1**: the contract balance does not exceed 2 tokens.

## Versions
- **v1**: compliant with the specification.

## Ground truths
|        | p1  |
|--------|-----|
| **v1** | 1   |
