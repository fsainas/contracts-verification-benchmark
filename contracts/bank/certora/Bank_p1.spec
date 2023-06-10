methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P1 {
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

// V1 proof: https://prover.certora.com/output/49230/9b05730d288a452abb7fda60e2d9af85?anonymousKey=5f1e42f7ed653e9f74a07a17bf1fc63d9766964e
// V2 proof: https://prover.certora.com/output/49230/1431ec42ca8a4c06b5b326a7efd7e864?anonymousKey=580d84d47f90b966ccd35dcfecef8c75f1aec908