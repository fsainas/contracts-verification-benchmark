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
        f.selector == withdraw().selector ||
        f.selector == reclaim().selector
    );

    
}