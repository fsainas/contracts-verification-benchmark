rule P1 {
    env e;
    assert releasable(e) <= getBalance();
}

// V1 proof: https://prover.certora.com/output/49230/d7489ea8303841b8baeff92d32267543?anonymousKey=1c313f52e25c02bea7b91fd2a1132bc13ed84a79