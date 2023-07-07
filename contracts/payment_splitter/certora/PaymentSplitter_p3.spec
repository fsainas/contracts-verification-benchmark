methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
}

rule P3 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) == 0;
}

rule NotP3 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) != 0;
}

// proof V1: 
!