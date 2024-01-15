rule withdraw_contract_balance {
    env e;
    uint256 amount;

    mathint old_contract_balance = getContractBalance();

    withdraw(e,amount);

    mathint new_contract_balance = getContractBalance();

    mathint amount_mathint = to_mathint(amount);
    assert new_contract_balance == old_contract_balance - amount_mathint;
}
