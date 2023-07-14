methods {
    function getOwner() external returns (address) envfree;
    function getRecovery() external returns (address) envfree;
}

rule P5 {
    require getOwner() != 0;
    require getRecovery() != 0;
    assert getOwner() != getRecovery();
}

rule NotP5 {
    require getOwner() != 0;
    require getRecovery() != 0;
    assert getOwner() == getRecovery();
}

// V1 proof: https://prover.certora.com/output/49230/b38e9cd5eb344096a161fd5a6d2f6e1f?anonymousKey=d7a8adad3b3eeaaaf4df42c817e0ca1110aaf808
// V2 proof: https://prover.certora.com/output/49230/0ff756ea67254234bd6a63662d4a7c03?anonymousKey=8dba94c14b7218a7050368f60a52d417344a483e
// V3 proof: https://prover.certora.com/output/49230/5793f2f4ea594c2abd30db0d0b7dfe05?anonymousKey=8cb5a0e83e740cf959165e82c6f2efd80c7ae8fb