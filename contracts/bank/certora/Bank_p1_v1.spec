methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
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

// proofs: https://prover.certora.com/output/49230/9b05730d288a452abb7fda60e2d9af85?anonymousKey=5f1e42f7ed653e9f74a07a17bf1fc63d9766964e