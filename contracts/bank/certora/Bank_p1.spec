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

rule NotP1 { // should fail
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

    assert totalBalanceAfter < senderBalanceAfter;
}

// V1 proof: https://prover.certora.com/output/49230/6a7ac915d2b24750925af49a22f2d652?anonymousKey=05ebfc45c45ad77a17e16214a5ce015165c7d43c
// V2 proof: https://prover.certora.com/output/49230/9739154ee47446149eecfc5326593d70?anonymousKey=17e746b647a4d6a7312d38d836591e334eeaf9af
// v3 proof: https://prover.certora.com/output/49230/a3770501293f42dba4da0bbfd9ffc320?anonymousKey=adc7bf94e0a2d0f8911b9f9158cfd751c2bead10