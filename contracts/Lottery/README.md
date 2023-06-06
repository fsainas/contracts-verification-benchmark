# Lottery

## Specification

This contract represents a simple lottery system. It allows participants to
enter the lottery by sending a specific amount of Ether and provides a function
to pick a winner among the entered participants.

The contract starts by defining a duration which will define the how much time
will pass between lottery rounds. 

An array called `players[]` tracks the addresses of the participants who have
entered the lottery.

The `enter()` function is used by participants to enter the lottery for the cost
of 0.01 Ether. It is an external function that can be called by anyone.

The `pickWinner()` function is also an external function that can be called by
anyone after the end of the round. It selects a winner by generating a
pseudo-random index within the range of the players array length and retrieves
the corresponding address. Upon invocation, the contract compensates the caller
with a fee and transfers the remaining balance to the winner. In the event of a
transfer failure, the contract reverts the transaction, enabling the selection
of a new winner. Ultimately, the players array is reset and new round begins.

## Properties

- **p1**: participants can enter the lottery
- **p2**: players can't be removed from the game until a winner is picked
- **p3**: if a player calls `enter()` and successfully sends 0.01 Ether, they
  can be selected as winner
- **p4**: the selected winner is always one of the eligible players

## Versions

- **v1**: conformant to specification

## Experiments

### SolCMC

|        | p1 | p2 | p3 | p4
| ------ | -- | -- | -- | --
| **v1** | TP | TP | ?  | ? 
