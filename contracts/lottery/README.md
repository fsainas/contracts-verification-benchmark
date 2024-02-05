# Lottery
This is a simplified version of [this](https://github.com/owanhunte/ethereum-solidity-course-updated-code/blob/main/lottery/contracts/Lottery.sol) contract by [@verumlotus](https://github.com/owanhunte).

## Specification
This contract represents a simple lottery system. It allows participants to
enter the lottery by sending a specific amount of Ether and provides a function
to pick a winner among the entered participants.

The contract starts by defining a duration which will define the how much time
will pass between lottery rounds. 

An array called `players[]` tracks the addresses of the participants who have
entered the lottery. 

The `enter()` function is used by participants to enter the lottery for the
cost of 0.01 Ether. It is an external function that can be called by anyone. 

The `pickWinner()` function is also an external function that can be called by
anyone after the end of the round. It selects a winner by generating a
pseudo-random index within the range of the players array length and retrieves
the corresponding address. Upon invocation, the contract compensates the caller
with a fee and transfers the remaining balance to the winner. In the event of a
transfer failure, the contract reverts the transaction, enabling the selection
of a new winner. Ultimately, the players array is reset and new round begins.


## Properties
- **add-player-only-enter**: the only way to be a member of the `players[]` array is to call `enter()`.
- **any-user-can-enter**: between the `start` and `start+duration` blocks, any user can join the lottery.
- **any-user-can-picker**: after the `start+duration` block, any user can choose to become the picker. If any does, a winner will eventually be picked.
- **enter-add-player**: if `enter()` is successfully called, the `msg.sender` is added to `players[]`.
- **enter-closes**: after the `start+duration` block, no user can join the lottery.
- **fairness**: among the users that have joined the lottery, the probability of any of them being selected as a winner is equal.
- **picker-paid**: the picker (if present) will eventually receive `0.01 * len(players[]) * 0.01` Ether.
- **players-permanent**: players can't be removed from the game until a winner is picked.
- **winner-paid**: the player that is selected as a winner will eventually receive `0.01 * len(players[]) * 0.99` Ether.

## Versions
- **v1**: conforming to specification.

## Ground truth
|        | add-player-only-enter | any-user-can-enter    | any-user-can-picker   | enter-add-player      | enter-closes          | fairness              | picker-paid           | players-permanent     | winner-paid           |
|--------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| **v1** | 1                     | 1                     | 1                     | 1                     | 0                     | 1                     | 1                     | 1                     | 1                     |
 

## Experiments
### SolCMC
#### Z3
|        | add-player-only-enter | any-user-can-enter    | any-user-can-picker   | enter-add-player      | enter-closes          | fairness              | picker-paid           | players-permanent     | winner-paid           |
|--------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| **v1** | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    |
 

#### Eldarica
|        | add-player-only-enter | any-user-can-enter    | any-user-can-picker   | enter-add-player      | enter-closes          | fairness              | picker-paid           | players-permanent     | winner-paid           |
|--------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| **v1** | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    | ND                    |
 


### Certora
|        | add-player-only-enter | any-user-can-enter    | any-user-can-picker   | enter-add-player      | enter-closes          | fairness              | picker-paid           | players-permanent     | winner-paid           |
|--------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| **v1** | FN                    | TP!                   | FN                    | FN                    | TN                    | ND                    | ND                    | FN                    | ND                    |
 

