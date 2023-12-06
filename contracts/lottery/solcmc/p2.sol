//p2
    function invariant(uint index) public view {
        require(msg.sender != address(0));
        require(players[index] == msg.sender);
        assert(_has_called_enter[msg.sender]);
    }

