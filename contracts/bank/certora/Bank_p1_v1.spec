methods {
    function getContractBalance() external returns (uint) envfree;
    function getBalance(address) external returns(uint) envfree;
    function receiveEth() external;
    function withdraw(uint) external;
}

/* 
 * contractBalanceAfter >= contractBalanceBefore after a payable function is
 * called is not considered by default
 */
rule contractBalanceGreaterOrEqualV1 {
    env e;
    address owner = e.msg.sender;
    
    uint256 addressBalanceBefore = getBalance(owner);
    uint256 contractBalanceBefore = getContractBalance();

    require contractBalanceBefore >= addressBalanceBefore;

    receiveEth(e);

    uint256 addressBalanceAfter = getBalance(owner);
    uint256 contractBalanceAfter = getContractBalance();

    //Cannot safely cast contractBalanceBefore + e.msg.value (mathint) to uint256
    require assert_uint256(contractBalanceBefore + e.msg.value) == contractBalanceAfter;

    assert contractBalanceAfter >= addressBalanceAfter;
}

rule contractBalanceGreaterOrEqualV2 {
    env e;
    address owner = e.msg.sender;
    
    uint256 addressBalanceBefore = getBalance(owner);

    receiveEth(e);

    uint256 contractBalance = getContractBalance();

    require assert_uint256(contractBalance - e.msg.value) >= addressBalanceBefore;

    uint256 addressBalanceAfter = getBalance(owner);

    assert contractBalance >= addressBalanceAfter;
}

rule contractBalanceEqual { // should fail
    env e;
    address owner = e.msg.sender;
    
    uint256 addressBalanceBefore = getBalance(owner);

    receiveEth(e);

    uint256 contractBalance = getContractBalance();

    require assert_uint256(contractBalance - e.msg.value) >= addressBalanceBefore;

    uint256 addressBalanceAfter = getBalance(owner);

    assert contractBalance == addressBalanceAfter;
}

// prover: https://prover.certora.com/output/49230/85e67c5be60a4076bdbf022b133fff2c?anonymousKey=92b17453867dd847b73f4d14b2a9e3aab939c113

