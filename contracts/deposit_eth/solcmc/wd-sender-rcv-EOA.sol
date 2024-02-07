/// @custom:preghost function withdraw
bool pre = msg.sender == tx.origin;
uint prev_sender_balance = address(msg.sender).balance;

/// @custom:postghost function withdraw
uint sender_balance = address(msg.sender).balance;	
assert(!pre || sender_balance == prev_sender_balance + amount);
