/// @custom:preghost function withdraw
uint old_user_balance = balances[msg.sender];

/// @custom:postghost function withdraw
uint new_user_balance = balances[msg.sender];
assert(new_user_balance == old_user_balance - amount);
