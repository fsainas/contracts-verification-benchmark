// SPDX-License-Identifier: GPL-3.0-only

rule withdraw_contract_balance {
    env e;
    uint256 amount;

    mathint old_contract_balance = balanceOf(currentContract);

    withdraw(e,amount);

    mathint new_contract_balance = balanceOf(currentContract);

    mathint amount_mathint = to_mathint(amount);
    assert new_contract_balance == old_contract_balance - amount_mathint;
}
