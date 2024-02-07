/// @custom:preghost function withdraw
uint old_user_balance = address(msg.sender).balance;

/// @custom:postghost function withdraw
uint new_user_balance = address(msg.sender).balance;
assert(new_user_balance == old_user_balance + amount);
