function invariant() public payable {
    // msg.value is already added to the contract balance upon calling invariant()
    uint old_contract_balance = address(this).balance - msg.value;
    deposit();
    uint new_contract_balance = address(this).balance;
    assert(new_contract_balance == old_contract_balance + msg.value);
}