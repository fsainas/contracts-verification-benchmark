rule P4 {
    env e;

    address sender = e.msg.sender;
    uint amount;
    
    mathint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    mathint senderBalanceAfterPlusAmount = getBalance(sender) + amount;
    
    assert senderBalanceBefore == senderBalanceAfterPlusAmount;
}
