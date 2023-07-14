methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function withdraw() external;
    function reclaim() external;
}

rule P4 {
    env e;
    calldataarg args;
    method f;
    
    require(e.block.number > getEndDonate());
    
    mathint before = getBalance();

    f(e, args);

    mathint after = getBalance();
    
    assert before > after => (
        f.selector == sig:withdraw().selector ||
        f.selector == sig:reclaim().selector
    );

    
}

// v1 proof: https://prover.certora.com/output/49230/d5485cfcbe434476ab40b1086045f25f?anonymousKey=ce1f140c23643660acd597f6f8b00634542e6154
