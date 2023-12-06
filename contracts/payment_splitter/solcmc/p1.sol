//p1

    function invariant(uint index) public view {
        require(index < payees.length);
        assert(payees[index] != address(0));
    }
