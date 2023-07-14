methods {
    function withdraw(address, uint) external;
    function finalize() external;
    function cancel() external;
    function getOwner() external returns (address) envfree;
    function getRecovery() external returns (address) envfree;
}

rule P2 {
    env e;
    address receiver;
    uint amount;
    cancel@withrevert(e);
    assert !lastReverted => e.msg.sender == getRecovery();
}

rule NotP2 {
    env e;
    cancel@withrevert(e);
    assert !lastReverted => e.msg.sender != getRecovery();
}

// V1 proof: https://prover.certora.com/output/49230/773800df3c3e43a9b31344b4ea2ae843?anonymousKey=97fadfce3ba98bf1a20219bf2a3945436dcd86980
// V2 proof: https://prover.certora.com/output/49230/41a4d0b3b2ff4cbd9587a8966fcabc56?anonymousKey=4672a7c56e4c395a6427957ea7e8c664b6c08f3b 
// V3 proof: https://prover.certora.com/output/49230/7d0046537ddf41a9a9980c4fde15714a?anonymousKey=1da569bc1fddd1477dcc477587dbae3044c9c2ae