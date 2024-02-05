ghost mapping(address => mathint) player_d {
    init_state axiom forall address a. player_d[a] == 0;
}

hook Sstore players[INDEX uint index] address addr (address old_value) STORAGE {
    player_d[addr] = player_d[addr] + 1;
    player_d[old_value] = player_d[addr] - 1;
}

rule players_permanent {
    address a;
    env e;
    method f;
    calldataarg args;

    require a != 0;
    require player_d[a] > 0;

    f(e, args); 
    
    require player_d[a] == 0;

    assert e.msg.sender == a && f.selector == sig:pickWinner().selector;
}
