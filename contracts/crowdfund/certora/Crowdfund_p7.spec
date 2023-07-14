methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
    function getGoal() external returns (uint) envfree;
    function withdraw() external;
    function reclaim() external;
    function donors(address) external returns (uint) envfree;
}

rule P7 {
    env e;
    calldataarg args;
    method f;
    
    require(e.block.number > getEndDonate());
    require(f.selector != sig:getBalance().selector);
    require(f.selector != sig:getEndDonate().selector);
    require(f.selector != sig:getGoal().selector);
    require(f.selector != sig:donors(address).selector);
    
    f(e, args);

    assert f.selector == sig:reclaim().selector || f.selector == sig:withdraw().selector;
}

// v1 proof: https://prover.certora.com/output/49230/c6c13d0dcc7e4a72ad9055ed6851c205?anonymousKey=a4657ece8bc91c19896d654420bac684e51346f3
