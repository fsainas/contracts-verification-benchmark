rule P2 {
    env e;
    uint amount;

    mathint before = getBalance();
    require before >= amount;
    
    withdraw(e, amount);
    
    mathint after = getBalance();
    assert before == after + amount;
}
