//p3
    function invariant(uint index) public view {
        assert(shares[payees[index]] > 0);
    }
