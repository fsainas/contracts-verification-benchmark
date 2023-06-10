methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

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

rule NotP2 { // should fail
    env e;
    method receive;
    calldataarg args;

    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);

    receive(e, args);

    uint256 senderBalanceAfter = getBalance(sender);

    assert e.msg.value == 0 <=> senderBalanceBefore < senderBalanceAfter;
}

// V1 proof: https://prover.certora.com/output/49230/f6a245fe2aaa4600ba71b4500f41717f?anonymousKey=fd893c109cc4b23e34426066cf17f05bd770f267
// V2 proof: https://prover.certora.com/output/49230/21f16acd4e8a4aa9b91f86a27a11a684?anonymousKey=e647f43c40d296b3b3957f6e328fe42ff392caf8