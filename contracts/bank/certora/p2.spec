rule P2 {
    env e;
    method receive;
    calldataarg args;

    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);

    receive(e, args);

    uint256 senderBalanceAfter = getBalance(sender);

    assert e.msg.value > 0 <=> senderBalanceBefore < senderBalanceAfter;
}
