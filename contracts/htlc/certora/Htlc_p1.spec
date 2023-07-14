methods {
       function getStart() external returns (uint) envfree;
       function getBalance() external returns (uint);
}

rule P1 {
    env e1;
    require e1.block.number == getStart();

    env e2;
    require e2.block.number > e1.block.number;
    
    assert getBalance(e1) >= getBalance(e2);
}

rule NotP1 {
    env e1;
    require e1.block.number == getStart();

    env e2;
    require e2.block.number > e1.block.number;
    
    assert getBalance(e1) < getBalance(e2);
}

// V1 proof: https://prover.certora.com/output/49230/fbf67611197848d39391ad27c9dac36d?anonymousKey=46ea3238e84a93b5579bd69b4c4f1408b590b557
// V2 proof: https://prover.certora.com/output/49230/4a5ad15eb3bd4901aba26f139977fd48?anonymousKey=1dbb496b6167640ee21203c72599dcbb2937fa30
// V3 proof: https://prover.certora.com/output/49230/4eed5a435f51429da65552e62827678d?anonymousKey=6e6b6c8046d9995378367a3eda745965df17d093
// V4 proof: https://prover.certora.com/output/49230/8f04f5405c5442eaa4a70695229c2ecc?anonymousKey=24575c61c53f8bdaf344a47ed0fb4d08805fae23
