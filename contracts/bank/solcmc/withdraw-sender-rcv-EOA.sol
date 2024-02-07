/// @custom:preghost function withdraw
bool pre = msg.sender == tx.origin;
uint old_user_balance = address(msg.sender).balance;

/// @custom:postghost function withdraw
uint new_user_balance = address(msg.sender).balance;
assert(!pre || new_user_balance == old_user_balance + amount);
