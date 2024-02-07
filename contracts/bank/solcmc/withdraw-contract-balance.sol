/// @custom:preghost function withdraw
uint old_contract_balance = address(this).balance;

/// @custom:postghost function withdraw
uint new_contract_balance = address(this).balance;
assert(new_contract_balance == old_contract_balance - amount);
