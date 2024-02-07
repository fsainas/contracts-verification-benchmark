/// @custom:preghost function deposit
uint old_user_balance = balances[msg.sender];

/// @custom:postghost function deposit
uint new_user_balance = balances[msg.sender];
assert(new_user_balance == old_user_balance + msg.value);
