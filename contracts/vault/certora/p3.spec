/// @custom:negate

rule P3 {
    env e1;
    address addr1;
    uint amt1;
    withdraw(e1, addr1, amt1);
    
    env e2;
    address addr2;
    uint amt2;
    withdraw@withrevert(e2, addr2, amt2);
    
    satisfy !lastReverted;
}
