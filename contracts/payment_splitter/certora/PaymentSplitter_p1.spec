methods {
    function getPayee(uint) external returns(address) envfree;
}

rule P1 {
    uint index;
    address addr = getPayee(index);
    //require !lastReverted;
    
    assert addr != 0;
}

rule NotP1 {
    uint index;
    address addr = getPayee(index);
    //require !lastReverted;
    
    assert addr == 0;
}

// V1 proof: 