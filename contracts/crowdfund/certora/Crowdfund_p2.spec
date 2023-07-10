methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function withdraw() external;
}

rule P2 {
    env e;
    
    require(getBalance() >= getGoal());
    require(e.block.number > getEndDonate());
    require(e.msg.value == 0);
    
    withdraw@withrevert(e);    

    assert !lastReverted;
}

rule NotP2 {
    env e;
    
    require(getBalance() >= getGoal());
    require(e.block.number < getEndDonate());
    require(e.msg.value == 0);
    
    withdraw@withrevert(e);    

    assert !lastReverted;
}