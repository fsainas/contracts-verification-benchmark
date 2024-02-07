/// @custom:preghost function withdraw
uint currb = balances[msg.sender];

/// @custom:postghost function withdraw
uint newb = balances[msg.sender];
assert(newb == currb - amount);
