// if B has at less than 1 token or he has already joined the bet, then he cannot deposit 1 token in the contract

/// @custom:preghost function deposit
bool pre = balance_b<1 || balance!=1;
int old_balance_b = balance_b;
int old_balance = balance;

/// @custom:postghost function deposit
assert (!pre || (balance_b==old_balance_b && balance==old_balance));
