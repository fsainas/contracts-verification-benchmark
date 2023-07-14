methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
}

rule P2 {
    env e;
    uint amount;

    mathint before = getBalance();
    require before == amount + 1;
    withdraw(e, amount);
    mathint after = getBalance();

    assert before == after + amount;
}

// V1 proof: https://prover.certora.com/output/49230/fc8a38ad4e6d4c549ae63dbdcff9804f?anonymousKey=b9f96764665f76a8f9da057509806d3d67db8f1e 
// V2 proof: https://prover.certora.com/output/49230/cd777d72f8ef498aa46b8c20e9b8b59b?anonymousKey=8eb28c1213f66173d629ca99c7c0a0daccd89160
// V3 proof: https://prover.certora.com/output/49230/b72a02488b684b08a02044bc2e19b68c?anonymousKey=7ad8d7cbdf932fe77cf9c40b6bee3ba6a7833389
// V4 proof: https://prover.certora.com/output/49230/540d6b1b01cf41e89385da572107b071?anonymousKey=36b884599eedc16216c69cf6721c8ff1107127ba
// V5 proof: https://prover.certora.com/output/49230/d35cb54cae6343919e14f4711b6ecd52?anonymousKey=88b2a45d7cc0fecc38492ba5482f74e0b19da38b