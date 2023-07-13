methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P3 {
    env e;
    calldataarg args;
    method f;

    uint amount;
    
    uint balanceBefore = getContractBalance();
    f(e, args);
    uint balanceAfter = getContractBalance();
    
    assert balanceBefore > balanceAfter => f.selector == sig:withdraw(uint).selector;
}

// proof V1: https://prover.certora.com/output/49230/c46fa5a2f80d4bdcac39c2fca5051e8c?anonymousKey=264e151e78b144a1f3344e906e8df4e4a067f95c
// proof V2: https://prover.certora.com/output/49230/a74dcea8456c46e2a77fb9d90560f923?anonymousKey=35b8c8db5b410695e168ad6a633a584217da2719
// proof V3: https://prover.certora.com/output/49230/1751f2ca11b84ec781e5b30a90560874?anonymousKey=c4829df37c94b00efe94d2d0681a7bdb300b3e46 
