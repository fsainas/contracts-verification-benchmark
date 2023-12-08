ghost mapping(uint => address) players; 
ghost uint playersLength;

hook Sload address addr players[INDEX uint index] STORAGE {
    require players[index] == addr;
}

hook Sstore playersLength uint lenNew STORAGE {
    // the length of a solidity storage array is at the variable's slot
    //playersLength = lenNew;
}

hook Sstore players[INDEX uint index] address addr STORAGE {
    players[index] = addr;
}

rule P3 {
    env e;
    
    require e.msg.value == 10^16;
    
    enter@withrevert(e);
    
    assert e.msg.sender == players[playersLength];

}

/*
rule NotP1 {
    env e;
    
    require e.msg.value == 10^16;
    
    enter@withrevert(e);
    
    assert e.msg.sender == getLastPlayer();
}
*/
