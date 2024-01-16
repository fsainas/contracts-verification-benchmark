rule wd_contract_bal {
    env e;
    uint amount;
    mathint mi_amount = amount;

    mathint before = getBalance();
    require before >= mi_amount;
    
    withdraw(e, amount);
    
    mathint after = getBalance();
    assert before == after + mi_amount;
}
