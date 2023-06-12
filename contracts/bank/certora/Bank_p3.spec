methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P3 {
    env e;

    address sender = e.msg.sender;
    uint amount;
    
    uint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    uint senderBalanceAfter = getBalance(sender);
    
    assert senderBalanceBefore > senderBalanceAfter;
}

// should fail
rule NotP3 {
    env e;

    address sender = e.msg.sender;
    uint amount;
    
    uint senderBalanceBefore = getBalance(sender);
    
    withdraw(e, amount);

    uint senderBalanceAfter = getBalance(sender);
    
    assert senderBalanceBefore <= senderBalanceAfter;
}

// proof V1: https://prover.certora.com/output/49230/b0692a36197f46cf8c65eaac820d3eba?anonymousKey=934acb96643456277d2daf4136a391a63a3fd1f7
// proof V2: https://prover.certora.com/output/49230/143f6491b0934c8781f7a691584319e5?anonymousKey=28f1f632c839d387ee1c275dbaae26a791151f3b
// proof V3: https://prover.certora.com/output/49230/2b8e10cde4094010a8a92d2bcba9fdc2?anonymousKey=0f255124c19263fcbb9d09ae527ee57978231615
// proof V4: https://prover.certora.com/output/49230/2cd6b595357640c6976d8e1bc005bd67?anonymousKey=702f8a7b255a9b6238f617cbfa83c7f1dee65cfa