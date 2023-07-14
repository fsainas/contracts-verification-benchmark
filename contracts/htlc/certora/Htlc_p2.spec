methods {
       function getStart() external returns (uint) envfree;
       function getIsCommitted() external returns (bool) envfree;
       function getBalance() external returns (uint);
       function commit(bytes32) external;
       function reveal(string) external;
       function timeout() external;
}

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

rule NotP2 {
    env e;
    calldataarg args;
    method f;

    f(e, args);

    assert (
        f.selector == sig:reveal(string).selector ||
        f.selector == sig:timeout().selector
    ) => !getIsCommitted();
}

// V1 proof: https://prover.certora.com/output/49230/bc59aa552c0f40c9937074e5eee69934?anonymousKey=b2c7311166d1eab116c5a295b406cfbb4f3e47a6
// V2 proof: 
