    // p4
    function invariant() public view {
        assert(state != States.REQ || address(this).balance >= amount);
    }
