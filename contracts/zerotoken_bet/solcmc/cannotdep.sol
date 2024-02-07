// if B has at less than 1 token or he has already joined the bet, then he cannot deposit 1 token in the contract

/// @custom:preghost function deposit
int old_balance_b = balance_b;
int old_balance = balance;
require (balance_b<1 || balance!=1);

/// @custom:postghost function deposit
assert (balance_b==old_balance_b && balance==old_balance);
