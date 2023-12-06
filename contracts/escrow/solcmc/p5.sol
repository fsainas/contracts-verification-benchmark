//p5
    function invariant() public view {
        require(_init_deposit > 0);
        require(fee_rate < 10000);
        require(buyer_choice != seller_choice);
        require(phase == Phase.END && escrow_choice != address(0));
        assert(_balance != deposit);
    }

