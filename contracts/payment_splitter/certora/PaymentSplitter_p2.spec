methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
}

rule P2 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) != 0;
}

rule NotP2 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) == 0;
}

// proof V1: https://prover.certora.com/output/49230/1e8ddc54c5f34a28a728017e5fced72b?anonymousKey=6603ffa4ab7c91fede7f25b3b393401ee8e10353
!