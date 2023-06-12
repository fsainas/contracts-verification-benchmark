methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P5 {
    env e;

    address sender = e.msg.sender;
    uint amount;

    mathint totalBalanceBefore = getContractBalance();
    mathint senderBalanceBefore = getBalance(sender);

    withdraw(e, amount);

    mathint totalBalanceAfter = getContractBalance();
    mathint senderBalanceAfter = getBalance(sender);
    
    assert totalBalanceBefore > totalBalanceAfter;
}

// should fail
rule notP5 {
    env e;

    address sender = e.msg.sender;
    uint amount;

    mathint totalBalanceBefore = getContractBalance();
    mathint senderBalanceBefore = getBalance(sender);

    withdraw(e, amount);

    mathint totalBalanceAfter = getContractBalance();
    mathint senderBalanceAfter = getBalance(sender);
    
    assert !(totalBalanceBefore > totalBalanceAfter);
}

// proof V1: https://prover.certora.com/output/49230/8d4ace7af61c48e5accdadb7c77a3382?anonymousKey=70608bccefb0a21f6065ba8ed756fa3cf6e84ce9
// proof V2: https://prover.certora.com/output/49230/7aa1a0c4c25a49bc8683977bb1275390?anonymousKey=7e546d0a3cec3b1c955204af22de2737de55cf1b
