methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
}

rule P3 {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}

rule NotP3 {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) == 0;
}

// proof V1: https://prover.certora.com/output/49230/989a1be40bdc41caa1921e791f00c2a9?anonymousKey=9bddb8d8136c81961402aa8f5002f16bde806bc6
