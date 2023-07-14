methods {
    function withdraw(address, uint) external;
    function finalize() external;
    function getOwner() external returns (address) envfree;
}

rule P1_withdraw {
    env e;
    address receiver;
    uint amount;
    withdraw@withrevert(e, receiver, amount);
    assert !lastReverted => e.msg.sender == getOwner();
}

rule P1_finalize {
    env e;
    finalize@withrevert(e);
    assert !lastReverted => e.msg.sender == getOwner();
}

rule NotP1_withdraw {
    env e;
    address receiver;
    uint amount;
    withdraw@withrevert(e, receiver, amount);
    assert !lastReverted => e.msg.sender != getOwner();
}

rule NotP1_finalize {
    env e;
    finalize@withrevert(e);
    assert !lastReverted => e.msg.sender != getOwner();
}

// V1 proof: https://prover.certora.com/output/49230/76d2fe2b6b5a4bbe917f678845f81e8c?anonymousKey=8a0b1d7da9b5ea18a5e7fb4bc078600c101592ba
// V2 proof: https://prover.certora.com/output/49230/c5ca9252f4294a7a8ac6295fa4bc1a13?anonymousKey=1dc96de838fd5191532be3882126a49d9895c30e
// V3 proof: https://prover.certora.com/output/49230/b173cfef13204c7aa10e4659443a940b?anonymousKey=6ede0abac95fe81d9c517cff1b2d561a879b04ee