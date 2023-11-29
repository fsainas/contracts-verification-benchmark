//p1
    function invariant() public view {
        require(!_picked);
        assert(players.length >= _prev_length);
    }
