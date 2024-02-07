/// @custom:preghost function deposit
// msg.value is already added to the contract balance upon call
uint old_contract_balance = address(this).balance - msg.value;

/// @custom:postghost function deposit
uint new_contract_balance = address(this).balance;
assert(new_contract_balance == old_contract_balance + msg.value);
