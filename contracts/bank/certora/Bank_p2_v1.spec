methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
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

// proof: https://prover.certora.com/output/49230/bed7b60650394c028127c8dfce4e3717?anonymousKey=0c31fa2d960b1a22984c544be86cddc83dc54df0
