methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
    function releasable(address) external returns(uint) envfree;
    function getBalance() external returns(uint) envfree;
}

rule P4 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert releasable(addr) <= getBalance();
}

rule NotP4 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) >= getBalance();
}

// proof V1:
