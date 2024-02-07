/// @custom:preghost function withdraw
uint prev_balance = address(this).balance  ;	

/// @custom:postghost function withdraw
assert(address(this).balance == prev_balance - amount);
