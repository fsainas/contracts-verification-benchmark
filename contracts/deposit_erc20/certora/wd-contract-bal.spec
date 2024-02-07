// SPDX-License-Identifier: GPL-3.0-only

rule wd_contract_bal {
    env e;
    uint amount;

    mathint before = getBalance();
    
    withdraw(e, amount);
    
    mathint after = getBalance();
    assert before == after + to_mathint(amount);
}
