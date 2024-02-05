rule wd_twice {
    env e1;
    address addr1;
    uint amt1;
    withdraw@withrevert(e1, addr1, amt1);
    
    satisfy !lastReverted;
    
    env e2;
    address addr2;
    uint amt2;
    withdraw@withrevert(e2, addr2, amt2);
    
    satisfy !lastReverted;
}
