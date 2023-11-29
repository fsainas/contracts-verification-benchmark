//p4
    function invariant() public view {
        assert(!(_current_phase == Phase.END) || _prev_phase == Phase.ARBITR || _prev_phase == Phase.REDEEM || _prev_phase == Phase.CHOOSE);
    }

