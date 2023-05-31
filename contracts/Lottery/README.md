# Lottery

## Specification

This contract represents a simple lottery system. It allows participants to
enter the lottery by sending a specific amount of Ether and provides a function
to pick a winner among the entered participants.

The contract starts by defining the `manager`, which is the address of the
account that deployed the contract and has the authority to pick the winner.
Additionally, an array called `players[]` tracks the addresses of the
participants who have entered the lottery.

The `enter()` function is used by participants to enter the lottery. It is an
external function that can be called by anyone. The cost of a ticket is 0.01
Ether. 

The `pickWinner()` function is a public function that can only be called by the
manager. It then selects a winner by generating a pseudo-random index within
the range of the players array length and retrieves the corresponding address.

Finally, the contract transfers the balance of the contract to the winner
address using the call function. The contract assumes that the winner address
is a regular Ethereum account capable of receiving funds. If the transfer
fails, the contract reverts the transaction and a new winner can be selected.

## Versions

- **v1**: conformant to specification
- **v2**: each player can only buy one ticket
- **v3**: *decentralized lottery*, there is no manager and the `pickWinner()`
  pays a fee to anyone how calls it
