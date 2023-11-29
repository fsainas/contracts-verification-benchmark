//p1
    function invariant() public view {
        assert(_fee <= _init_deposit);
    }
