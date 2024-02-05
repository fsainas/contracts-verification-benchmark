
methods {
    function enter() external;
    function getLastPlayer() external returns (address) envfree;
    function getPlayersLength() external returns (uint) envfree;
    function pickWinner() external;
}
ghost mapping(address => mathint) player_d {
    init_state axiom forall address a. player_d[a] == 0;
}

hook Sstore players[INDEX uint index] address addr (address old_value) STORAGE {
    player_d[addr] = player_d[addr] + 1;
    player_d[old_value] = player_d[addr] - 1;
}

rule enter_add_player {
    address a;
    env e;

    require a != 0;
    mathint prev = player_d[a];

    enter(e);
    
    assert player_d[a] > prev;

}
