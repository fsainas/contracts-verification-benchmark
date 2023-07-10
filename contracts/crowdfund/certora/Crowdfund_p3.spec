methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function withdraw() external;
}

rule P3 {
    env e;
    
    require(e.block.number > getEndDonate());
    
    mathint before = getBalance();
    mathint after = getBalance();
    
    assert before >= after;
    
}

rule NotP3 {
    env e;
    
    require(e.block.number > getEndDonate());
    
    mathint before = getBalance();
    mathint after = getBalance();
    
    assert before == after;
    
}