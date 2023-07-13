methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P6 {
    env e;

    uint amount;
    
    require amount > getBalance(e.msg.sender);
    withdraw@withrevert(e, amount);
    
    assert lastReverted;
}

// proof V1: https://prover.certora.com/output/49230/7fc352cab5a44b53ba2a0d48290fb126?anonymousKey=516436db3724f9277ae7d9c2ac199076324e0466
// proof V2: https://prover.certora.com/output/49230/9cc210fb60b14b04b3418917cd169d24?anonymousKey=4903a925c09eac3cc2d600f575a4599f9823123b
// proof V3: https://prover.certora.com/output/49230/655b87579f4c4ee9ba720b57503a146f?anonymousKey=14606df12eae5f14d3f5cac7417df724b0afb3ff
