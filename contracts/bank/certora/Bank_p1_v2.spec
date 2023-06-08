methods {
    function getContractBalance() external returns (uint) envfree;
    function getBalance(address) external returns(uint) envfree;
    function withdraw(uint) external;
}

rule totalBalanceGreaterOrEqual {
    env e;
    method receive;
    calldataarg args;

    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);
    uint256 totalBalanceBefore = getContractBalance();

    require totalBalanceBefore >= senderBalanceBefore;

    receive(e, args);

    uint256 senderBalanceAfter = getBalance(sender);
    uint256 totalBalanceAfter = getContractBalance();

    assert totalBalanceAfter >= senderBalanceAfter;
}

rule totalBalanceEqual { // should fail
    env e;
    method receive;
    calldataarg args;

    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);
    uint256 totalBalanceBefore = getContractBalance();

    require totalBalanceBefore >= senderBalanceBefore;

    receive(e, args);

    uint256 senderBalanceAfter = getBalance(sender);
    uint256 totalBalanceAfter = getContractBalance();

    assert totalBalanceAfter == senderBalanceAfter;
}

// prover:https://prover.certora.com/output/49230/cee0fa9e72214701b86faee70025266f?anonymousKey=ad5a438a053b593047216ec8c320040fb6d5d2d8 