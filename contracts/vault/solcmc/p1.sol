    // p1
    function invariant_withdraw(address receiver_, uint amount_) public {
        withdraw(receiver_, amount_);
        assert(msg.sender == owner);
    }

    // p1
    function invariant_finalize() public {
        finalize();
        assert(msg.sender == owner);
    }
