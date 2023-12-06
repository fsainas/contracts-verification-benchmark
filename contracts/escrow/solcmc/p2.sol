//p2
    function invariant() public view {
        assert(!(_current_phase == Phase.REDEEM) || _prev_phase == Phase.CHOOSE);
    }
