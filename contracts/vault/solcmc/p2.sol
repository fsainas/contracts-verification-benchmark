   // p2
    function invariant() public {
        cancel();
        assert(msg.sender == recovery);
    }
    
    
