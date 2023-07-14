methods {
       function getEverDeposited() external returns (bool);
       function getSupply() external returns (uint);
       function getR0() external returns (uint);
       function getR1() external returns (uint);
}

rule P1 {
    env e;
    assert getEverDeposited(e) => getR0(e) > 0 && getR1(e) > 0;
}

rule NotP1 {
    env e;
    assert getEverDeposited(e) => getR0(e) == 0 && getR1(e) == 0;
}

// V1 proof: https://prover.certora.com/output/49230/8a40987800f245298a276e8a19d7e647?anonymousKey=fa7bc25b557862ad65038589dc6ef3c7b94d87c7