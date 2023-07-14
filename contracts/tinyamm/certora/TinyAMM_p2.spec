methods {
       function getEverDeposited() external returns (bool);
       function getSupply() external returns (uint);
       function getR0() external returns (uint);
       function getR1() external returns (uint);
}

rule P2 {
    env e;
    assert getEverDeposited(e) => getSupply(e) > 0;
}

rule NotP2 {
    env e;
    assert getEverDeposited(e) => getSupply(e) == 0;
}

// V1 proof: https://prover.certora.com/output/49230/83d0063cf1ad4d26903f1f4661a30fb9?anonymousKey=51ac9d0199e49a65ddf197c7f9f11ff0360e5705