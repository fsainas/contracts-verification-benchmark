function invariant(address addr) public {
    assert(contract_balance >= balances[addr]);
}
