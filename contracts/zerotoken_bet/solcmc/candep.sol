// before the deadline, if B has at least 1 token and he has not joined the bet yet, 
// then he can deposit 1 token in the contract

/// @custom:preghost function deposit
bool pre = block.number <= timeout_block && balance_b>=1 && balance==1;
int old_balance_b = balance_b;

/// @custom:postghost function deposit
assert (!pre || (balance_b==old_balance_b-1 && balance==2));
