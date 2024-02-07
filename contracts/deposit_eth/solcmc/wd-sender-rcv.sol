/// @custom:preghost function withdraw
uint prev_sender_balance = address(msg.sender).balance;

/// @custom:postghost function withdraw
uint sender_balance = address(msg.sender).balance;	
assert(sender_balance == prev_sender_balance + amount);
