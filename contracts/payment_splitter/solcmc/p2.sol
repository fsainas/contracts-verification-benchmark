//p2
    function invariant(address addr) public view {
        assert(!(payees[0] == addr) || shares[addr] == 0);
    }
