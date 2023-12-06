rule P1 {
    uint index;
    address addr = getPayee(index);
    //require !lastReverted;
    
    assert addr != 0;
}

