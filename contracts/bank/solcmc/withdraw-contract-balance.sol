function invariant(uint amount) public payable {
    uint old_contract_balance = address(this).balance - msg.value;
    withdraw(amount);
    uint new_contract_balance = address(this).balance;

    assert(new_contract_balance == old_contract_balance - amount);
}
