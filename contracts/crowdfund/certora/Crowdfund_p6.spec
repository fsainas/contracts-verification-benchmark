methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function getReceiver() external returns (address) envfree;
    function withdraw() external;
    function reclaim() external;
}

rule P6 {
    env e;
    method f;
    calldataarg args;
    
    require e.block.number > getEndDonate();
    require getBalance() >= getGoal();
    mathint balance_before = getBalance();
    f(e, args);
    mathint balance_after = getBalance();
    
    assert balance_before > balance_after => (
        f.selector == sig:withdraw().selector &&
        e.msg.sender == getReceiver()
        );
}

// v1 proof: https://prover.certora.com/output/49230/272642d07977495b831416b68f11b8a8?anonymousKey=2c288d6b97f87a14f01a63663a10411fbd898827
