/// @custom:postghost function withdraw
assert(!(amount == 0 || amount > balances[msg.sender]));
