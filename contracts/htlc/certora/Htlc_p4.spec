methods {
       function getStart() external returns (uint) envfree;
       function getIsCommitted() external returns (bool) envfree;
       function getBalance() external returns (uint);
       function commit(bytes32) external;
       function reveal(string) external;
       function timeout() external;
}

rule P3 {
    env e1;
    require e1.block.number == getStart();

    env e2;
    timeout(e2);
    mathint block_number = e2.block.number;
    
    assert block_number > e1.block.number + 1000;
}

rule NotP3 {
    env e1;
    require e1.block.number == getStart();

    env e2;
    timeout(e2);
    mathint block_number = e2.block.number;

    assert block_number <= e1.block.number + 1000;
}

// V1 proof: https://prover.certora.com/output/49230/5de91047560e48868e26c72186ace14c?anonymousKey=3a0a8a3f8e8b4aa3e531501e848bc215904903d9
// V2 proof: 
// V3 proof: https://prover.certora.com/output/49230/86a779beae9f45e38c51923b72c641d1?anonymousKey=3c92120deed1f3cb84e902f0d71d8cf554d1671a
