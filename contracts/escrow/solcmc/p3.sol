//p3
     function invariant() public view {
        assert(!(_current_phase == Phase.ARBITR) || _prev_phase == Phase.REDEEM);
    }

