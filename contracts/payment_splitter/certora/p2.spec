rule P2 {
    address addr;
    
    require getPayee(0) == addr;
    
    assert getShares(addr) == 0;
}

