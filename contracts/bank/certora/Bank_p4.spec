methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P4 {
    env e;

    address sender = e.msg.sender;
    uint amount;
    
    mathint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    mathint senderBalanceAfterPlusAmount = getBalance(sender) + amount;
    
    assert senderBalanceBefore == senderBalanceAfterPlusAmount;
}

// should fail
rule NotP4 {
    env e;

    address sender = e.msg.sender;
    uint amount;
    
    mathint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    mathint senderBalanceAfterPlusAmount = getBalance(sender) + amount;
    
    assert senderBalanceBefore != senderBalanceAfterPlusAmount;
}

// proof V1: https://prover.certora.com/output/49230/34fb8131416e46f59f9127fd193f1136?anonymousKey=1adfe521d361cb02c9706a9d04eb0fdacfd750b2
// proof V2: https://prover.certora.com/output/49230/5b94c88b14644752b3f0a8278cb31106?anonymousKey=ef7473ba1ee917bf1ebceaa4a9d68d7393ffc423
// proof V3: https://prover.certora.com/output/49230/7960b58e22324fba89baa7e320684af5?anonymousKey=4ceb946dd5eea019ff0c8d2677419bf0a34d9cdb