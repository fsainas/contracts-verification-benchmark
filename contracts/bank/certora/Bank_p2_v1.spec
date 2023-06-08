methods {
    function getBalance(address) external returns(uint) envfree;
    function withdraw(uint) external;
}

rule SenderBalanceDecreased {
    env e;
    address sender = e.msg.sender;
    uint amount;
    
    uint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    uint senderBalanceAfter = getBalance(sender);
    
    assert senderBalanceBefore > senderBalanceAfter;
}

// should fail
rule SenderBalanceEqual {
    env e;
    address sender = e.msg.sender;
    uint amount;
    
    uint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    uint senderBalanceAfter = getBalance(sender);
    
    assert senderBalanceBefore == senderBalanceAfter;
}

// should fail
rule SenderBalanceIncreased {
    env e;
    address sender = e.msg.sender;
    uint amount;
    
    uint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    uint senderBalanceAfter = getBalance(sender);
    
    assert senderBalanceBefore < senderBalanceAfter;
}

// proof: https://prover.certora.com/output/49230/69f54448631648e5ab905a1d000ff538?anonymousKey=b5b1777c200c98fbcbdac3dbb11ec5b84d5eb237
