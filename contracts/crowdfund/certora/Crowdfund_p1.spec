methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function withdraw() external;
}

rule P1 {
    env e;
    
    uint balance = getBalance();
    uint goal = getGoal();
    require balance < goal;
    
    withdraw@withrevert(e);    

    assert lastReverted;
}

rule NotP1 {
    env e;
    
    uint balance = getBalance();
    uint goal = getGoal();
    require balance > goal;
    
    withdraw@withrevert(e);    

    assert lastReverted;
}

// V1 proof: https://prover.certora.com/output/49230/0deab5e13ab348a4983e81915953e6f9?anonymousKey=dde2a41e8c8ffb7ae7713a353543f26f0fab4089