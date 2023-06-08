methods {
    function getContractBalance() external returns (uint) envfree;
    function getBalance(address) external returns(uint) envfree;
    function receiveEth() external;
    function withdraw(uint) external;
}

rule totalBalanceGreaterOrEqual {
    env e;
    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);
    uint256 totalBalanceBefore = getContractBalance();

    require totalBalanceBefore >= senderBalanceBefore;

    receiveEth(e);

    uint256 senderBalanceAfter = getBalance(sender);
    uint256 totalBalanceAfter = getContractBalance();

    assert totalBalanceAfter >= senderBalanceAfter;
}

rule totalBalanceEqual {
    env e;
    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);
    uint256 totalBalanceBefore = getContractBalance();

    require totalBalanceBefore >= senderBalanceBefore;

    receiveEth(e);

    uint256 senderBalanceAfter = getBalance(sender);
    uint256 totalBalanceAfter = getContractBalance();

    assert totalBalanceAfter == senderBalanceAfter;
}

// prover: https://prover.certora.com/output/49230/1b8a1e9ce6c9413e81dbb843017034bb?anonymousKey=dee48afa7b35740a3ba130c09d2da14fcd24d3ed


