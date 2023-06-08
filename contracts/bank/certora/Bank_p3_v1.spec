methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
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

// proof: https://prover.certora.com/output/49230/724461f104c6412490e6dafb00f1cd0c?anonymousKey=65fdc022b616f4fc7191349cf1efdc5c53cd2103