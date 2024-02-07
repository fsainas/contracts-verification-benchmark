/// @custom:preghost function deposit
uint currb = balances[msg.sender];

/// @custom:postghost function deposit
uint newb = balances[msg.sender];
assert(newb == currb + amount);
