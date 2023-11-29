//p4
    function invariant(uint index) public view {
        assert(releasable(payees[index]) <= address(this).balance);
    }
