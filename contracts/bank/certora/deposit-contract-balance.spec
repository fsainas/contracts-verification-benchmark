rule deposit_contract_balance {
    env e;

    mathint old_contract_balance = getContractBalance();

    deposit(e);

    mathint new_contract_balance = getContractBalance();

    mathint deposit_amount = to_mathint(e.msg.value);
    assert new_contract_balance == old_contract_balance + deposit_amount;
}
