methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
    function releasable(address) external returns(uint) envfree;
    function getBalance() external returns(uint) envfree;
    function getTotalReleasable() external returns(uint) envfree;
}

rule P5 {
    assert getTotalReleasable() == getBalance();
}

rule NotP5 {
    assert getTotalReleasable() != getBalance();
}

// V1 proof: https://prover.certora.com/output/49230/d11de96f34d14b6497de40a728a64eca?anonymousKey=d7cd2a3792d932e1104554884f41ef3064594968
