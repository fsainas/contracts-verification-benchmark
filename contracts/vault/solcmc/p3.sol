    // p3
    function invariant() public view {
        assert(!_used || _prev != state);	
    }
