methods {
    function getEndDonate() external returns (uint) envfree;
    function getBalance() external returns (uint);
}

rule P3 {
    env e1;
    env e2;

    require e1.block.number > getEndDonate();
    require e2.block.number > getEndDonate();
    require e1.block.number < e2.block.number;
    
    mathint balance1 = getBalance(e1);
    mathint balance2 = getBalance(e2);
    
    assert balance1 == balance2;
}

rule NotP3 {
    env e1;
    env e2;

    require e1.block.number > getEndDonate();
    require e2.block.number > getEndDonate();
    require e1.block.number < e2.block.number;
    
    mathint balance1 = getBalance(e1);
    mathint balance2 = getBalance(e2);
    
    assert balance1 != balance2;
}

// V1 proof: https://prover.certora.com/output/49230/272516faa43541b38264186b338ee5ed?anonymousKey=6a659efbca8e3798b7a96ec1790a7b6f073b6200