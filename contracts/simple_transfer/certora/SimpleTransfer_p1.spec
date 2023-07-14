methods {
    function getBalance() external returns (uint);
    function withdraw(uint) external;
}

rule P1 {
    env e1;
    env e2;

    require e1.block.number < e2.block.number;

    mathint balance1 = getBalance(e1);
    mathint balance2 = getBalance(e2);

    assert balance1 >= balance2;
}

rule NotP1 {
    env e1;
    env e2;

    require e1.block.number < e2.block.number;

    mathint balance1 = getBalance(e1);
    mathint balance2 = getBalance(e2);

    assert balance1 < balance2;
}

// V1 proof: https://prover.certora.com/output/49230/4f56405552f14c81995f562df1195274?anonymousKey=1e99ba5a7feedafd31d9de986c7ec3c4bd5fd358
// V2 proof: https://prover.certora.com/output/49230/f3169cc0c8194c3eaf4b3da2099febb3?anonymousKey=5b52f3c8d92e91691b80a60c8e62aca2dbdf67b0
// V3 proof: https://prover.certora.com/output/49230/01514e888e2441e79a97d7acf9a1d7f0?anonymousKey=bcab5ca4863da0d874b35331112804ed72678047
// V4 proof: https://prover.certora.com/output/49230/c85478f9c4af4fdbbe587ecc6070468a?anonymousKey=9b5a3258e607699693206a546bd44c92f1f01950
// V5 proof: https://prover.certora.com/output/49230/5c2ef2bbc8e743bbb0626f1426d1529e?anonymousKey=e1a39504221c4b66082acb957e8896b78a0198ad