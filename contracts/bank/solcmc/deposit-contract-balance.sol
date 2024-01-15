function invariant() public payable {
    uint old_contract_balance = address(this).balance;
    
    deposit();
    
    uint new_contract_balance = address(this).balance;
    
    assert(new_contract_balance == old_contract_balance + msg.value);
}
