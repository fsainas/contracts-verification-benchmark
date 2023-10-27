rule P2 {
    env e;
    calldataarg args;
    method f;

    f(e, args);

    assert (
        f.selector == sig:reveal(string).selector ||
        f.selector == sig:timeout().selector
    ) => getIsCommitted();

}

// V1 proof: https://prover.certora.com/output/49230/bc59aa552c0f40c9937074e5eee69934?anonymousKey=b2c7311166d1eab116c5a295b406cfbb4f3e47a6
// V2 proof: https://prover.certora.com/output/49230/01faf6931a4a48cd9aee170574093c91?anonymousKey=948acb867be8bbae00f874cb8c22ef52a3c8d8c2
// V3 proof: https://prover.certora.com/output/49230/d4792a5b719d42d89ba0edf9980cd276?anonymousKey=cd32c23a31357ad748ee554da97c25f91ddc6fcd
// V4 proof: https://prover.certora.com/output/49230/3c395ac8a9664e3092346c749c3623f6?anonymousKey=9860fb7a065c6317f8e1a48fa5dd5873cf2cad9f
