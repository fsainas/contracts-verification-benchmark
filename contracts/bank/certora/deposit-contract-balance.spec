// SPDX-License-Identifier: GPL-3.0-only

rule deposit_contract_balance {
    env e;

    mathint old_contract_balance = balanceOf(currentContract);
    deposit(e);
    mathint new_contract_balance = balanceOf(currentContract);

    assert new_contract_balance == old_contract_balance + to_mathint(e.msg.value);
}
