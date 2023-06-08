methods {
    function getBalance(address) external returns(uint) envfree;
    function withdraw(uint) external;
}

rule SenderBalanceDecreasedByAmount {
    env e;
    address sender = e.msg.sender;
    uint amount;
    
    mathint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    mathint senderBalanceAfterPlusAmount = getBalance(sender) + amount;
    
    assert senderBalanceBefore == senderBalanceAfterPlusAmount;
}

// should fail
rule SenderBalanceNotDecreasedByAmount {
    env e;
    address sender = e.msg.sender;
    uint amount;
    
    mathint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    mathint senderBalanceAfterPlusAmount = getBalance(sender) + amount;
    
    assert senderBalanceBefore != senderBalanceAfterPlusAmount;
}

// proof: https://prover.certora.com/output/49230/0e9e154c78fd4b6b8a08ab6dcad31da4?anonymousKey=98f4c057538250a750c9638a84a70062f999669f
